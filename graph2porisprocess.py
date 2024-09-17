
import csv, os, re
from bs4 import BeautifulSoup
from pyexcel_ods import save_data
from collections import OrderedDict
from pathlib import Path
from config_csys import *

# Importing test configuration file
import config
from graph2porislib import *

file_data = ['','']
localcsids = {}
inverse_localcsids = {}

def get_project_ancestors(thisproject,rootproject,projects):
  if (thisproject.id != rootproject.id):
    parentproj = None
    if hasattr(thisproject,'parent'):
      print("The parent id to find for",thisproject.identifier,"is",thisproject.parent.id)
      for p in projects:
        if p.id == thisproject.parent.id:
          parentproj = p
          break

    else:
      print("The project",thisproject.identifier,"has no parent",dict(thisproject))
    
    if parentproj is not None:
      result = get_project_ancestors(parentproj,rootproject,projects)
      result += [thisproject] 

    else:      
      print("Error, we could not find the parent of ",thisproject.identifier)
      #result = [thisproject]
      assert(False)
  
  else:
    # If thisproject is the root project, we have finished    
    result = [thisproject]

  return result

def get_project_successors(thisproject,projects):
  result = []
  for p in projects:
    if hasattr(p,'parent'):
      if p.parent.id == thisproject.id:
        result += [p] + get_project_successors(p,projects)

  return result

def get_project_tree(thisproject,rootproject,projects):
  # First we will add the ancestors
  result = get_project_ancestors(thisproject,rootproject,projects)

  # Then we will add the successors
  result += get_project_successors(thisproject,projects)
  
  return result


def create_ods_file_from_graphml_file(filename, deviceName):
  global file_data
  global localcsids
  global inverse_localcsids

  with open(filename) as file:
    soup = BeautifulSoup(file, 'lxml-xml')
    graph = soup.find("graph",{"id":"G"})
    nodes = soup.findAll("node", {"yfiles.foldertype":""})
    groups = soup.find_all("node", {"yfiles.foldertype":"group"})
    edges = soup.findAll("edge")
    urlkey = soup.find("key",{"attr.name":"url"})['id']
    csidkey = soup.find("key",{"attr.name":"csID"})['id']
    cscodekey = soup.find("key",{"attr.name":"csCode"})['id']
    csprjident = soup.find("key",{"attr.name":"identifier"})['id']
    csrootprjident = soup.find("key",{"attr.name":"rootid"})['id']
    csparentCSIDident = soup.find("key",{"attr.name":"parentCSID"})['id']
    csrmid = soup.find("key",{"attr.name":"rmID"})['id']

  print("url key",urlkey)
  print("csid key",csidkey)
  print("parentCSID key",csparentCSIDident)

  # Retrieving file_data
  file_data = graph.find_all('data')
  file_cscode = ""
  file_identifier = ""
  file_root_identifier = ""
  parent_csys_identifier = ""
  
  for n in file_data:
    print(n['key'])
    if n['key'] == cscodekey:
      if len(n.contents) >= 1:
        thiscontent = n.contents[0].strip()
        if len(thiscontent) > 0:                
          file_cscode = thiscontent
      
      else:
        file_cscode = 'INS'
    
    if n['key'] == csprjident:
      if len(n.contents) >= 1:
        thiscontent = n.contents[0].strip()
        if len(thiscontent) > 0:                
          file_identifier = thiscontent        

      else:
        file_identifier = 'instrument'

    if n['key'] == csrootprjident:
      if len(n.contents) >= 1:
        thiscontent = n.contents[0].strip()
        if len(thiscontent) > 0:                
          file_root_identifier = thiscontent        

      else:
        file_root_identifier = 'instrument'


    if n['key'] == csparentCSIDident:
      if len(n.contents) >= 1:
        thiscontent = n.contents[0].strip()
        if len(thiscontent) > 0:                
          parent_csys_identifier = thiscontent        

      else:
        parent_csys_identifier = ''

  print("csCode:",file_cscode)
  print("identifier:",file_identifier)
  print("root_identifier:",file_root_identifier)
  print("parent_csys_identifier:",parent_csys_identifier)

  continueProcess = False
  if not csys_use:
    continueProcess = True
  else:
    import requests as req
    prcfdict = {}
    cfdict = {}
    rmissues = {}
    from redminelib import Redmine

    if csys_ignorecert:
        redmine = Redmine(csys_server_url,key=csys_key_txt, requests={'verify': False})
    else:
        redmine = Redmine(csys_server_url,key=csys_key_txt)

    projects = redmine.project.all()


    print("Proyectos:")
    for p in projects:
        print("    ",p.identifier,"     | ",p.name)
        if p.identifier == file_identifier:
          continueProcess = True

    if continueProcess:
      continueProcess = False
      my_project = redmine.project.get(file_identifier)
      if my_project is None:
        print("No podemos obtener el proyecto")
      else:
        print ("Obtenemos proyecto: ",my_project.identifier," | ",my_project.name)

      my_root_project = redmine.project.get(file_root_identifier)
      if my_root_project is None:
        print("No podemos obtener el proyecto raíz")
      else:
        print ("Obtenemos proyecto raíz: ",my_root_project.identifier," | ",my_root_project.name)

        # Now we obtain the csCode
        for cf in my_project.custom_fields:
          print(cf)
          prcfdict[cf.name] = cf
          if cf.name == "csCode":
            file_cscode = cf.value
            print("csCode:",file_cscode)

        cfields = redmine.custom_field.all()
        for cf in cfields:
          print(cf)
          cfdict[cf.name] = cf

        project_tree = get_project_tree(my_project,my_root_project,projects)

        for p in project_tree:
          print(p.identifier)

        rm_issues_dict = {}
        for p in project_tree:
          for i in p.issues:
            i_ident = i.custom_fields.get(cfdict['csID'].id).value
            rm_issues_dict[i_ident] = i
            print(i_ident,i.subject)

        continueProcess = True

  if continueProcess:
    # First we must find the roots

    roots = []
    groups_dict = {}
    global_dict = {}
    csv_dict_data = []
    error_list = []
    nodes_graphml_d6 = {}
    nodes_graphml_url = {}
    nodes_graphml_rmid = {}
    nodes_graphml = {}
    rm_issues_created = []

    for group in groups:
      group_dict = {}
      group_dict['min'] = None
      group_dict['default'] = None
      group_dict['max'] = None
      group_dict['group_id'] = group['id']
      group_dict['csID'] = group['id']
      group_name = group.find('y:NodeLabel').text.strip()
      group_dict['url'] = ""
      group_dict['rmid'] = ""

      group_data = group.findChildren('data',recursive=False)
      #print("+++",group_name)
      nodes_graphml[group['id']] = group

      # Prevent having rmide and not having csid (error in removing csID an not removing rmid)
      thisrmid = None
      thisrmidcontent = None
      hascsid = False
      hasrmid = False
      
      for n in group_data:
        if n['key']==csidkey:
          nodes_graphml_d6[group['id']] = n
          if len(n.contents) >= 1:
            hascsid = True
            thiscontent = n.contents[0].strip()
            if len(thiscontent) > 0:
              group_dict['csID'] = thiscontent
              localcsids[group_dict['group_id']] = group_dict['csID']
              if group_dict['csID'] not in inverse_localcsids.keys():
                inverse_localcsids[group_dict['csID']] = group_dict['group_id']

              else:
                error_list += [group_dict['csID'] +" identifier is not unique, check "+  group_name + " and " + global_dict[inverse_localcsids[group_dict['csID']]]['group_name']  ]
                print(error_list)

        if n['key']==urlkey:
          #print("***",group_name,n.contents)
          nodes_graphml_url[group['id']] = n
          if len(n.contents) >= 1:
            thiscontent = n.contents[0].strip()
            if len(thiscontent) > 0:            
              group_dict['url'] = thiscontent
              #group_dict['rmid'] = n.contents[0].split('/')[-1]

        if n['key']==csrmid:
          #print("***",group_name,n.contents)
          if len(n.contents) >= 1:
            thisrmid = n
            thiscontent = n.contents[0].strip()
            if len(thiscontent) > 0:
              thisrmidcontent = thiscontent
              hasrmid = True

      # Prevent having rmide and not having csid (error in removing csID an not removing rmid)
      if hascsid and hasrmid:
        nodes_graphml_rmid[group['id']] = thisrmid
        group_dict['rmid'] = thisrmidcontent

      group_dict['group_name'] = group_name
      # The group can be a prSys, or a prParam, or a prValueFloat
      group_shape = group.find('y:Shape')['type'].strip()
      group_dict['shape'] = group_shape
      if group_shape == "parallelogram":
        group_dict['node_type'] = "prValFloat"

      else:
        if group_shape == "roundrectangle":
          # We must know if it is a prSys or a prParam
          # prParam: <y:Fill color="#CAECFF84" transparent="false"/>
          group_color_attribute = group.find('y:Fill')
          if group_color_attribute is not None:
            if group_color_attribute.get('color') is not None:
              group_color = group_color_attribute['color'].strip()
              if group_color == "#CAECFF84":
                group_dict['node_type'] = "prParam"
              
              else:
                group_dict['node_type'] = "prSys"
              
            else:
              group_dict['node_type'] = "prSys"

      group_id_parts = re.findall(r'n\d{1,}', group_dict['group_id'])

      if(len(group_id_parts) > 1):
        group_dict['parent_group_id'] = convert_list_to_string(group_id_parts[:-1], '::')
        #print("parent_group",group_dict['parent_group_id'],groups_dict[group_dict['parent_group_id']]['group_name'])
        group_dict['parent_group_name'] = groups_dict[group_dict['parent_group_id']]['group_name']
      else:
        roots += [group_dict]
        group_dict['parent_group_id'] = None
        group_dict['parent_group_name'] = ""

      groups_dict[group_dict['group_id']] = group_dict
      global_dict[group_dict['group_id']] = group_dict


      nodes_dict = {}


    # Prevent having rmide and not having csid (error in removing csID an not removing rmid)
    thisrmid = None
    thisrmidcontent = None
    hascsid = False
    hasrmid = False
      
    for node in nodes:
        ischild = False
        isMax = False
        isMin = False
        isDefault = False
        node_dict = {}
        node_dict['node_type'] = "unknown"
        node_dict['node_id'] = node['id']
        node_id_parts = re.findall(r'n\d{1,}', node_dict['node_id'])
        node_dict['node_group_id'] = convert_list_to_string(node_id_parts[:-1], '::')
        node_dict['node_name'] = node.find('y:NodeLabel').text.strip()
        node_data = node.findChildren('data',recursive=False)
        node_dict['min'] = None
        node_dict['default'] = None
        node_dict['max'] = None
        node_dict['defaulttext'] = None
        node_dict['rmid'] = ""
        node_dict['url'] = ""
        node_dict['relations'] = []
        node_dict['next'] = []
        node_dict['csID'] = node['id']
        node_shape = node.find('y:Shape')['type'].strip()
        #print(node_dict['node_name'],node_shape)
        nodes_graphml[node['id']] = node
        for n in node_data:
          if n['key']==csidkey:
            nodes_graphml_d6[node['id']] = n
            if len(n.contents) >= 1:
              thiscontent = n.contents[0].strip()
              if len(thiscontent) > 0:
                node_dict['csID'] = thiscontent
                localcsids[node_dict['node_id'] ] = node_dict['csID']
                if node_dict['csID'] not in inverse_localcsids.keys():
                  inverse_localcsids[node_dict['csID']] = node_dict['node_id']

                else:
                  error_list += [node_dict['csID'] +" identifier is not unique, check "+  node_dict['node_name'] + " and " + global_dict[inverse_localcsids[node_dict['csID']]]['node_name']  ]

          if n['key']==urlkey:
            nodes_graphml_url[node['id']] = n
            if len(n.contents) >= 1:
              thiscontent = n.contents[0].strip()
              if len(thiscontent) > 0:                
                node_dict['url'] = thiscontent

          if n['key']==csrmid:
            #print("***",group_name,n.contents)
            thisrmid = n
            if len(n.contents) >= 1:
              thiscontent = n.contents[0].strip()
              if len(thiscontent) > 0:
                thisrmidcontent = thiscontent
                hasrmid = True

        # Prevent having rmide and not having csid (error in removing csID an not removing rmid)
        if hascsid and hasrmid:
          nodes_graphml_rmid[node['id']] = thisrmid
          node_dict['rmid'] = thisrmidcontent

        color_attribute = node.find('y:Fill')
        node_color = None
        if color_attribute is not None:
          if color_attribute.get('color') is not None:
            node_color = color_attribute['color'].strip()

        if node_shape == "parallelogram":
          if node_color is not None:
            if node_color == "#99CCFF":
              node_dict['node_type'] = "prValue"

            else:
              if node_color == "#CCCCFF":
                node_dict['node_type'] = "prValFloat"
                second_label = node.find('y:NodeLabel',{"textColor":"#0000FF"}).text.strip()
                valueslist = second_label.split('≤')
                if len(valueslist) == 1:
                  valueslist = second_label.split('<')
                
                #print(">>>>>>",valueslist)
                node_dict['min'] = float(valueslist[0].strip())
                node_dict['default'] = float(valueslist[1].strip())
                node_dict['max'] = float(valueslist[2].strip())

              else:
                if node_color == "#CCFFCC":
                  # This is prValueText
                  node_dict['node_type'] = "prValText"
                  second_label = node.find('y:NodeLabel',{"textColor":"#FF0000"}).text.strip()
                  node_dict['defaulttext'] = second_label

          else:
            print("Not recognized, TODO.")
            

        else:
          if node_shape == "roundrectangle":
            node_dict['node_type'] = "prMode"

          else:
            if node_shape == "ellipse":
              node_dict['node_type'] = "prCmd"

        node_tree = []

        if('parent_group_name' in groups_dict[node_dict['node_group_id']]):
          node_tree.append(groups_dict[node_dict['node_group_id']]['parent_group_name'])
          node_dict['node_group_name'] = groups_dict[node_dict['node_group_id']]['parent_group_name']
          #node_dict['node_type'] = groups_dict[node_dict['node_group_id']]['node_type']
          #node_dict['node_group_sort_order'] = groups_dict[node_dict['node_group_id']]['parent_group_sort_order']
        else:
          node_dict['node_group_name'] = groups_dict[node_dict['node_group_id']]['group_name']
          #node_dict['node_group_sort_order'] = groups_dict[node_dict['node_group_id']]['group_sort_order']

        node_tree.append(groups_dict[node_dict['node_group_id']]['group_name'])
        node_tree.append(node_dict['node_name'])
        node_tree_text = convert_list_to_string(node_tree, ' > ')
        #node_tree_text = node_tree_text + ' (' + str(groups_dict[node_dict['node_group_id']]['group_sort_order']) + ')'

        nodes_dict[node_dict['node_id']] = node_dict
        global_dict[node_dict['node_id']] = node_dict
        csv_dict_data.append(node_dict)

    if len(error_list) <= 0:

      for key in groups_dict:
        group_dict = groups_dict[key]
        node_dict = {}
        node_dict['node_id'] = group_dict['group_id']
        node_dict['node_name'] = group_dict['group_name']
        node_dict['node_group_id'] = group_dict['parent_group_id']
        node_dict['node_group_name'] = group_dict['parent_group_name']
        node_dict['node_type'] = group_dict['node_type']
        node_dict['min'] = group_dict['min']
        node_dict['default'] = group_dict['default']
        node_dict['max'] = group_dict['max']
        node_dict['defaulttext'] = group_dict['default']
        node_dict['url'] = group_dict['url']
        node_dict['rmid'] = group_dict['rmid']
        node_dict['relations'] = []
        node_dict['next'] = []
        node_dict['csID'] = group_dict['csID']
        nodes_dict[node_dict['node_id']] = node_dict

        csv_dict_data.append(node_dict) 


      for e in edges:
        for d in e.find_all('data'):
          #print("-->",d)
          polyline = d.find('y:PolyLineEdge')
          #print("polyline",polyline)
          if polyline is not None:
            linestile = polyline.find('y:LineStyle')#['type']
            if linestile is not None:
              if linestile['color'] == "#FF9900":
                nodes_dict[e['source']]['relations'] += [e['target']]
              else:
                nodes_dict[e['source']]['next'] += [e['target']]

      
      data = OrderedDict() # from collections import OrderedDict
      
      print(localcsids)

      if csys_use:
        trackerdict = {}
        trackers = redmine.tracker.all()
        for tr in trackers:
            trackerdict[tr.name] = tr

      rows = [['RM#','url','RMID','ID','row#','subject','','tracker','Rlv?','status','parent',
      'blocking_items','precedent_items','prMin','prDefault','prMax','prDefaultText','version','priority']]
      rmtranslator = {}

      for n in csv_dict_data:
        rmissueneeded = False
        if csys_use:
          # See if the id exists in redmine
          if n['csID'] not in rm_issues_dict.keys():
            print("NO",n['csID'],rm_issues_dict.keys())
            rmissueneeded = True

          else:
            rmtranslator[n['node_id']] = n['csID']


        if rmissueneeded:
          rm_issues_created += [n['node_id']]
          print("New rmissue for ", n['node_id'])
          thistrackerid = trackerdict[n['node_type']].id
          thisRmTsk = redmine.issue.create(project_id = my_project.id,
              tracker_id = thistrackerid,
              subject = n['node_name'],
          )
          url = csys_server_url+'/issues/'+str(thisRmTsk.id)
          urlwithkey= url +'?key='+csys_key_txt
          resp = req.get(urlwithkey)
          thisRmTsk = redmine.issue.get(thisRmTsk.id)
          thisCsId = thisRmTsk.custom_fields.get(cfdict['csID'].id).value
          rm_issues_dict[thisCsId] = thisRmTsk
          rmtranslator[n['node_id']] = thisCsId
          print("------------------------->",n['node_id'],thisCsId)
          n['rmid'] = thisRmTsk.id
          n['url'] = url
      
      print("******************************************************************")
      print(rmtranslator)
      for n in csv_dict_data:
        row = []
        thisgroup = n['node_group_id']
        if thisgroup is not None:
          print("orig",thisgroup)
          if csys_use:
            if thisgroup in rmtranslator.keys():
              thisgroup = rmtranslator[thisgroup]
          else:
            if thisgroup in localcsids.keys():
              thisgroup= localcsids[thisgroup]

        relstr = ""
        first = True
        for c in n['relations']:
          if not first:
            relstr += ", "
          else:
            first = False
          
          relid = c
          if csys_use:
            if relid in rmtranslator.keys():
              relid = rmtranslator[relid]
          else:
            if relid in localcsids.keys():
              relid = localcsids[relid]
          

          relstr += relid

        n['relations'] = relstr

        relstr = ""
        first = True
        for c in n['next']:
          if not first:
            relstr += ", "
          else:
            first = False
          
          relid = c
          if csys_use:
            if relid in rmtranslator.keys():
              relid = rmtranslator[relid]
          else:
            if relid in localcsids.keys():
              relid = localcsids[relid]
          
          relstr += relid
        
        n['next'] = relstr

        strparent = ''
        if thisgroup is not None:
          strparent = thisgroup

        else:
          # If the item has no parent, then its parent if shall be 
          # the parentCSID of the project, because a partial diagram must always
          # belong to a parent system
          strparent = parent_csys_identifier

        strrel = ''
        if n['relations'] is not None:
          strrel = n['relations']

        strnext = ''
        if n['next'] is not None:
          strnext = n['next']

        strmin = ''
        if n['min'] is not None:
          strmin = n['min']

        strdefault = ''
        if n['default'] is not None:
          strdefault = n['default']

        strmax = ''
        if n['max'] is not None:
          strmax = n['max']

        strdefaulttext = ''
        if n['defaulttext'] is not None:
          strdefaulttext = n['defaulttext']

        thisid = n['node_id']
        if csys_use:
          if thisid in rmtranslator.keys():
            thisid = rmtranslator[thisid]

        else:
          if thisid in localcsids.keys():
            thisid = localcsids[thisid]
          

        row += [[n['rmid'],n['url'],n['rmid'],thisid,'',n['node_name'],'',n['node_type'],'','',
          strparent,strrel,strnext,strmin,strdefault,strmax,strdefaulttext,'','Normal']]

        '''
        row += [[n['relations'],n['next'],n['default'],n['max']]]
        '''
        
        rows += row


      data.update({"Dict": [['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',5,'',len(csv_dict_data)+1]
      , ['',''], ['',''], ['',file_identifier], ['',file_cscode]]})
      data.update({"Items": rows})
      data.update({"ExtraFields":[[]]})


      dirname = os.path.dirname(filename)
      basenamelist = os.path.splitext(os.path.basename(filename))
      onlyname = basenamelist[0]
      extension = basenamelist[1]
      odsextension = ".ods"
        

      save_data(os.path.join(dirname,onlyname+odsextension), data)

      print(">>>>",nodes_graphml_d6)

      if False and csys_use:
      # ONGOING PROCESS
        
        for k in global_dict.keys():
          item = global_dict[k]
          ident = item['csID']
          rm = rm_issues_dict[ident]
          if 'relations' in item.keys():
            relations = item['relations']
          
          else:
            relations = ""
            
          print(ident, rm.subject,rm.tracker.name, "[", relations, "]")
          print(rm.relations)

          rels = relations.split(',')
          print(rels)

          rel_existentes = {}
          for ir in rm.relations:
            print(dict(ir))
            if ir.relation_type == 'blocks':
              rel_existentes[str(ir.issue_id)] = ir

          for r in rels:
            r = r.strip()
            if len(r) > 1:
              other_rm = rm_issues_dict[r]
              if str(other_rm.id) in rel_existentes.keys():
                print("Ya existe la relación, la quit ode la lista de relaciones existentes")
                rel_existentes.pop(str(other_rm.id))
                
              else:
                print("Hemos de crear la relación de bloqueo entre la issue ", rm.id," y la issue ", other_rm.id)
                relat = redmine.issue_relation.create(
                  issue_id=other_rm.id,
                  issue_to_id=rm.id,
                  relation_type='blocks')
                
                
          for k in rel_existentes.keys():
            print("Debería borrar la relación con ", ir.issue_to_id)
            redmine.issue_relation.delete(ir.id)
          
        
        
        
        print("\nItero por las creadas",rm_issues_created)
        print("\nd6",nodes_graphml_d6.keys())
        print("\npadres",nodes_graphml.keys())
        for k in rm_issues_created:
            if k in nodes_graphml_d6.keys():
              nodes_graphml_d6[k].contents[0].replace_with(rmtranslator[k])
            
            else:
              new_tag = soup.new_tag('data',key=csidkey)
              new_tag.string = rmtranslator[k]
              nodes_graphml[k].append(new_tag)

        for k in nodes_dict.keys():
            thisurl = nodes_dict[k]['url']
            if thisurl=="":
              thisurl = csys_server_url+'/issues/'+str(rm_issues_dict[rmtranslator[k]].id)

            if k in nodes_graphml_url.keys():
              nodes_graphml_url[k].string = thisurl
            
            else:
              new_tag = soup.new_tag('data',key=urlkey)
              new_tag.string = thisurl
              nodes_graphml[k].append(new_tag)

            thisrmid = nodes_dict[k]['rmid']
            if thisrmid=="":
              thisrmid = str(rm_issues_dict[rmtranslator[k]].id)

            if k in nodes_graphml_rmid.keys():
              nodes_graphml_rmid[k].string = str(thisrmid)
            
            else:
              new_tag = soup.new_tag('data',key=csrmid)
              new_tag.string = str(thisrmid)
              nodes_graphml[k].append(new_tag)


        with open(os.path.join(dirname,onlyname+extension+'.out'), "w", encoding='utf-8') as file:
            file.write(str(soup))


    else:
      print("ERROR!\nERROR!\nERROR!\nERROR!")
      print("Identifiers inconsistency errors: ")
      for e in error_list:
        print(e)

      print("\n\nPROCESS CANCELLED (identifiers)\n\n\n")

  else:
    print("\n\nPROCESS CANCELLED\n\n\n")

