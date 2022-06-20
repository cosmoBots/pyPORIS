# Note, thanks to https://github.com/viperior/graphml-interpreter
import argparse
from locale import normalize                     # This library allows us to easily parse the command line arguments
import pathlib

import csv, os, re
from bs4 import BeautifulSoup
from pyexcel_ods import save_data
from collections import OrderedDict
from config_csys import *

# Importing test configuration file
import config
from graph2porislib import *
import glob

debug2JSON = False

if debug2JSON:
  import json

def gettypeabbrev(t):
  if t == "prSys":
    return "s#"
  if t == "prValue":
    return "v#"
  if t == "prValFloat":
    return "vf#"
  if t == "prMode":
    return "m#"
  if t == "prParam":
    return "p#"
  if t == "prValText":
    return "vt#"
  if t == "prCmd":
    return "c#"

def create_local_path(ndict,key):
  #print("create path for",key)
  n = ndict[key]
  path = gettypeabbrev(n['node_type'])+n['name']
  if 'node_group_id' in n.keys():
    if len(n['node_group_id'])>0:
      path = create_local_path(ndict,n['node_group_id']) + '/' + path

  return path

def create_global_path(ndict,key,project):
  print("create path for",key,"of project",project)
  n = ndict[key]
  if n['project'] == project:
    path = gettypeabbrev(n['node_type'])+n['name']
    if 'node_group_id' in n.keys():
      if len(n['node_group_id'])>0:
        thispath = create_global_path(ndict,n['node_group_id'],project)
        if thispath != None:
          path  = thispath + '/' + path

    return path

  else:
    return None

def create_tree_from_graphml_dir(dirname, deviceName):
  #print(dirname+'/*.graphml')
  filenames = glob.glob(dirname+'/*.graphml')
  #print(filenames)

  data = OrderedDict() # from collections import OrderedDict
  rows = [['RM#','url','RMID','ID','row#','subject','','tracker','Rlv?','status','parent',
  'blocking_items','precedent_items','prMin','prDefault','prMax','prDefaultText','version','priority','filename','external']]

  global_dict= {}
  normalized_dict = {}
  node_aliases = {}
  inverse_aliases = {}
  csys_dict = {}
  global_file_identifier = ""
  global_file_cscode = ""
  graphml_csid_nodes_fileid = {}
  graphml_url_nodes_fileid = {}
  graphml_rmid_nodes_fileid = {}
  graphml_project_nodes_fileid = {}

  # If we need to sync with cosmoSys, we will try to open the cosmoSys server at the beginning, to avoid later problems
  continueProcess = True

  if csys_use:
    continueProcess = False

    import requests as req
    prcfdict = {}
    cfdict = {}
    from redminelib import Redmine

    if csys_ignorecert:
        cosmosys = Redmine(csys_server_url,key=csys_key_txt, requests={'verify': False})
    else:
        cosmosys = Redmine(csys_server_url,key=csys_key_txt)

    trackerdict = {}
    trackers = cosmosys.tracker.all()
    for tr in trackers:
        trackerdict[tr.name] = tr


    projects = cosmosys.project.all()

    csys_projects = {}
    csys_issues = {}
    csys_prj_dict = {}
    csys_issues_created = {}
    filesoups = {}

    print("Projects:")
    for p in projects:
        print("\t",p.identifier," \t| ",p.name)
        csys_prj_dict[p.identifier] = p
        if p.identifier == deviceName:
          continueProcess = True

    if continueProcess:
      continueProcess = False
      rootproject = cosmosys.project.get(deviceName)
      if rootproject is None:
        print("We can not obtain the root project for this GraphML folder")
      else:
        print ("Root project found at cosmoSys server: ",rootproject.identifier," | ",rootproject.name)
        continueProcess = True
        csys_projects[deviceName] = rootproject

        # Now we obtain the csCode
        for cf in rootproject.custom_fields:
          prcfdict[cf.name] = cf
          if cf.name == "csCode":
            file_cscode = cf.value

        cfields = cosmosys.custom_field.all()
        for cf in cfields:
          cfdict[cf.name] = cf

        rm_issues_dict = {}
        for i in rootproject.issues:
          i_ident = i.custom_fields.get(cfdict['csID'].id).value
          rm_issues_dict[i_ident] = i    

  if continueProcess:
    for filename in filenames:
      basefilename = Path(filename).stem
      #print("---------------------",basefilename,"------------------------------")
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
        csparentident = soup.find("key",{"attr.name":"parentid"})['id']
        csrootident = soup.find("key",{"attr.name":"rootid"})['id']
        csrmid = soup.find("key",{"attr.name":"rmID"})['id']
        csproject = soup.find("key",{"attr.name":"project"})['id']

      #print("url key",urlkey)
      #print("csid key",csidkey)

      # Retrieving file_data
      file_data = graph.find_all('data')
      file_cscode = ""
      file_identifier = ""
      for n in file_data:
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
            file_cscode = 'instrument'

      if deviceName == basefilename:
        global_file_identifier = file_identifier
        global_file_cscode = file_cscode
      
      #print("csCode:",file_cscode)
      #print("identifier:",file_identifier)

      # Create the local tree
      groups_dict = {}

      for group in groups:
        group_node = {}
        group_node['group_id'] = group['id']
        group_node['group_name'] = group.find('y:NodeLabel').text.strip()
        group_id_parts = re.findall(r'n\d{1,}', group_node['group_id'])

        if(len(group_id_parts) > 1):
          group_node['parent_group_id'] = convert_list_to_string(group_id_parts[:-1], '::')
          group_node['parent_group_name'] = groups_dict[group_node['parent_group_id']]['group_name']

        groups_dict[group_node['group_id']] = group_node

      nodes_dict = {}

      for node in nodes + groups:
        normal_node = {}
        normal_node['nodeid'] = node['id']
        nodeid_parts = re.findall(r'n\d{1,}', normal_node['nodeid'])
        normal_node['node_group_id'] = convert_list_to_string(nodeid_parts[:-1], '::')
        normal_node['name'] = node.find('y:NodeLabel').text.strip()

        if len(normal_node['node_group_id'])>0:
          normal_node['parentkey'] = basefilename + '/' + normal_node['node_group_id']
          normal_node['alternative_parent'] = None

        else:
          normal_node['parentkey'] = None
          normal_node['alternative_parent'] = basefilename + '/' + normal_node['node_group_id']

        if node not in groups:
          if('parent_group_name' in groups_dict[normal_node['node_group_id']]):
            normal_node['node_group_name'] = groups_dict[normal_node['node_group_id']]['parent_group_name']
          else:
            normal_node['node_group_name'] = groups_dict[normal_node['node_group_id']]['group_name']
        

        node_shape = node.find('y:Shape')['type'].strip()
        normal_node['shape'] = node_shape
        normal_node['csID'] = None
        normal_node['min'] = None
        normal_node['default'] = None
        normal_node['max'] = None
        normal_node['defaulttext'] = None
        normal_node['project'] = None
        normal_node['rmid'] = 0
        normal_node['url'] = ""
        normal_node['relations'] = []
        normal_node['next'] = []
        normal_node['node_type'] = None
        normal_node['external'] = False      
        normal_node['filename'] = basefilename
        normal_node['globalid'] = basefilename + '/' + normal_node['nodeid']

        node_data = node.findChildren('data',recursive=False)
        csiddatanode = None
        rmiddatanode = None
        urldatanode = None
        projectdatanode = None
        for n in node_data:
          if n['key']==csidkey:
            csiddatanode = n
            if len(n.contents) >= 1:
              thiscontent = n.contents[0].strip()
              if len(thiscontent) > 0:
                normal_node['csID'] = thiscontent

          if n['key']==urlkey:
            urldatanode = n
            if len(n.contents) >= 1:
              thiscontent = n.contents[0].strip()
              if len(thiscontent) > 0:                
                normal_node['url'] = thiscontent
            
          if n['key']==csrmid:
            rmiddatanode = n
            if len(n.contents) >= 1:
              thiscontent = n.contents[0].strip()
              if len(thiscontent) > 0:
                normal_node['rmid'] = thiscontent

          if n['key']==csproject:
            projectdatanode = n
            if len(n.contents) >= 1:
              thiscontent = n.contents[0].strip()
              if len(thiscontent) > 0:            
                normal_node['project'] = thiscontent
                if normal_node['project'] != basefilename:
                  normal_node['external'] = True

        if csiddatanode is None:
          csiddatanode = soup.new_tag('data',key=csidkey)
          csiddatanode.string = ""
          node.append(csiddatanode)
        
        if rmiddatanode is None:
          rmiddatanode = soup.new_tag('data',key=csrmid)
          rmiddatanode.string = ""
          node.append(rmiddatanode)

        if urldatanode is None:
          urldatanode = soup.new_tag('data',key=urlkey)
          urldatanode.string = ""
          node.append(urldatanode)

        if projectdatanode is None:
          projectdatanode = soup.new_tag('data',key=csproject)
          projectdatanode.string = ""
          node.append(projectdatanode)

        graphml_csid_nodes_fileid[normal_node['globalid']] = csiddatanode
        graphml_url_nodes_fileid[normal_node['globalid']] = rmiddatanode
        graphml_rmid_nodes_fileid[normal_node['globalid']] = urldatanode
        graphml_project_nodes_fileid[normal_node['globalid']] = projectdatanode

        if node not in groups:
          color_attribute = node.find('y:Fill')
          node_color = None
          if color_attribute is not None:
            if color_attribute.get('color') is not None:
              node_color = color_attribute['color'].strip()

          if node_shape == "parallelogram":
            if node_color is not None:
              if node_color == "#99CCFF":
                normal_node['node_type'] = "prValue"

              else:
                if node_color == "#CCCCFF":
                  normal_node['node_type'] = "prValFloat"
                  second_label = node.find('y:NodeLabel',{"textColor":"#0000FF"}).text.strip()
                  valueslist = second_label.split('≤')
                  if len(valueslist) == 1:
                    valueslist = second_label.split('<')
                  
                  #print(">>>>>>",valueslist)
                  normal_node['min'] = float(valueslist[0].strip())
                  normal_node['default'] = float(valueslist[1].strip())
                  normal_node['max'] = float(valueslist[2].strip())

                else:
                  if node_color == "#CCFFCC":
                    # This is prValueText
                    normal_node['node_type'] = "prValText"
                    second_label = node.find('y:NodeLabel',{"textColor":"#FF0000"}).text.strip()
                    normal_node['defaulttext'] = second_label

            else:
              print("Not recognized, TODO.")
              

          else:
            if node_shape == "roundrectangle":
              normal_node['node_type'] = "prMode"

            else:
              if node_shape == "ellipse":
                normal_node['node_type'] = "prCmd"

        else:
          if node_shape == "roundrectangle":
            # We must know if it is a prSys or a prParam
            # prParam: <y:Fill color="#CAECFF84" transparent="false"/>
            print("AAAAAAAAAAAAAA proceso grupo",normal_node['name'],node_shape)
            group_color_attribute = node.find('y:Fill')
            if group_color_attribute is not None:
              if group_color_attribute.get('color') is not None:
                group_color = group_color_attribute['color'].strip()
                if group_color == "#CAECFF84":
                  normal_node['node_type'] = "prParam"
                
                else:
                  normal_node['node_type'] = "prSys"
                
              else:
                normal_node['node_type'] = "prSys"        


        if csys_use:
          # Let's take the information for this and other modules in the same project
          if normal_node['csID'] is not None:
            if normal_node['csID'] not in csys_issues.keys():
              # The csys node has not been downloaded to the csys_issues dictionary,
              # probably the project has not been downloaded
              thisnodeprojectkey = normal_node['project']
              if thisnodeprojectkey not in csys_projects.keys():
                # The project nodes have not been added to the csys_issues dictionary
                if thisnodeprojectkey not in csys_prj_dict.keys():
                  print("Error, the node has a project identifier which is not present in the cosmoSys server")
                  return None
                
                else:
                  # We add the project to the csys_projects dictionary
                  thisproject = csys_prj_dict[normal_node['project']]
                  csys_projects[thisnodeprojectkey] = thisproject
                  # We add all its csys nodes to the csys_issues dictionary
                  for i in thisproject.issues:
                    i_ident = i.custom_fields.get(cfdict['csID'].id).value
                    if i_ident not in csys_issues.keys():
                      csys_issues[i_ident] = {}
                      csys_issues[i_ident]['csys'] = i
                      csys_issues[i_ident]['nodes'] = [normal_node]

                    else:
                      csys_issues[i_ident]['nodes'] += [normal_node]

            else:
              # After all this downloading process, both the node project and the csys node have to exist in corresonding dictionaries
              if normal_node['csID'] not in csys_issues.keys():
                print("Error, the node has a csID which is not present in the cosmoSys server")
                return None
              if normal_node['project'] not in csys_projects.keys():
                print("Error, the node has a project which is not present in the cosmoSys server")
                return None

          else:
            print("We have to create a new DB identifier for",normal_node['name'],"at project",normal_node['project'],"we are processing the diagram",basefilename)
            if normal_node['project'] != basefilename:
              print("BUT this is not the place to do it (",basefilename,"), we will need to do it when processing the diagram for the project "+normal_node['project'])

            else:
              print("This is the perfect place to do it!!!",basefilename)
              print("New csys_issue for ", normal_node['name'], "in project",normal_node['project'])
              # First we ensure we have the project
              thisnodeprojectkey = normal_node['project']
              if thisnodeprojectkey not in csys_projects.keys():
                # The project nodes have not been added to the csys_issues dictionary
                if thisnodeprojectkey not in csys_prj_dict.keys():
                  print("Error, the node has a project identifier which is not present in the cosmoSys server")
                  return None
                
                else:
                  # We add the project to the csys_projects dictionary
                  thisproject = csys_prj_dict[normal_node['project']]
                  csys_projects[thisnodeprojectkey] = thisproject

              else:
                thisproject = csys_projects[thisnodeprojectkey]    

              # Let's see the 
              thistrackerid = trackerdict[normal_node['node_type']].id
              thisCsysIss = cosmosys.issue.create(project_id = thisproject.id,
                  tracker_id = thistrackerid,
                  subject = normal_node['name'],
              )
              url = csys_server_url+'/issues/'+str(thisCsysIss.id)
              urlwithkey= url +'?key='+csys_key_txt
              resp = req.get(urlwithkey)
              thisCsysIss = cosmosys.issue.get(thisCsysIss.id)
              thisCsId = thisCsysIss.custom_fields.get(cfdict['csID'].id).value
              normal_node['csID'] = thisCsId
              normal_node['rmid'] = thisCsysIss.id
              normal_node['url'] = url
              csys_issues_created[thisCsId] = normal_node
              # We will update the node where it was supposed to be the csID
              n = graphml_csid_nodes_fileid[normal_node['globalid']]
              n.contents[0].replace_with(normal_node['csID'])
              # updating rmid
              n = graphml_rmid_nodes_fileid[normal_node['globalid']]
              n.contents[0].replace_with(str(normal_node['rmid']))
              # updating url
              n = graphml_url_nodes_fileid[normal_node['globalid']]
              n.contents[0].replace_with(normal_node['url'])
              # updating project
              n = graphml_project_nodes_fileid[normal_node['globalid']]
              n.contents[0].replace_with(normal_node['project'])


        nodes_dict[normal_node['nodeid']] = normal_node
        global_dict[normal_node['globalid']] = normal_node

      # At this point we have the nodes for the current file
      # Let's calculate their paths
      for key in nodes_dict.keys():
        normal_node = nodes_dict[key]
        normal_node['nodepath'] = basefilename + '/' + create_local_path(nodes_dict,key)
        normal_node['globalpath'] = normal_node['project'] + '/' + create_global_path(nodes_dict,key,normal_node['project'])

      # Now we have to express the edges in globalpath language
      for e in edges:
        for d in e.find_all('data'):
          #print("-->",d)
          polyline = d.find('y:PolyLineEdge')
          #print("polyline",polyline)
          if polyline is not None:
            linestile = polyline.find('y:LineStyle')#['type']
            if linestile is not None:
              if linestile['color'] == "#FF9900":
                nodes_dict[e['source']]['relations'] += [basefilename + '/' + e['target']]
              else:
                nodes_dict[e['source']]['next'] += [basefilename + '/' + e['target']]

      # Adding the XML "soup" of the current file to the filesoups dictionary
      # in order to allow final changes after all the file loop has been done
      filesoups[basefilename] = soup

    # Once we have the global_dict with all the nodes and the adressing system, let's create the normalized dict
    # and the node aliases that will be used for relationships
    for key in global_dict:
      normal_node = global_dict[key]
      if not normal_node['external']:
        normal_node['normalized_relations'] = []
        normal_node['normalized_next'] = []
        normalized_dict[normal_node['globalpath']] = normal_node

      node_aliases[normal_node['globalid']] = normal_node['globalpath']
      if normal_node['external']:
        if normal_node['globalpath'] not in inverse_aliases.keys():
          inverse_aliases[normal_node['globalpath']] = [normal_node['globalid']]

        else: 
          inverse_aliases[normal_node['globalpath']] += [normal_node['globalid']]

    # In the case a normalized node is the root of its drawing, the parent must be taken from the external references

    if debug2JSON:
      out_file = open("node_aliases.json", "w")
      json.dump(node_aliases, out_file, indent=4)
      out_file.close()  

      out_file = open("inverse_aliases.json", "w")
      json.dump(inverse_aliases, out_file, indent=4)
      out_file.close()  

      out_file = open("normalized_dict.json", "w")
      json.dump(normalized_dict, out_file, indent=4)
      out_file.close()
         

    # And now, we have to re-link the relationships to the normalized targets
    for key in global_dict:
      normal_node = global_dict[key]
      normalized_node = normalized_dict[node_aliases[key]]
      for r in normal_node['relations']:
        normalized_node['normalized_relations'] += [node_aliases[r]]

      for r in normal_node['next']:
        normalized_node['normalized_next'] += [node_aliases[r]]

    if debug2JSON:
      out_file = open("global_dict.json", "w")
      json.dump(global_dict, out_file, indent=4)
      out_file.close()

    # At this moment, we have finished all the relationships and we are about to create the output file
    # We will use the information in the csID attributes to translate the keys to be written on it

    translator_dict = {}
    for key in normalized_dict.keys():
      n = normalized_dict[key]
      if n['csID'] is not None:
        translator_dict[key] = n['csID']

    ## At this moment, we have a good opportunity to sync the changes with the cosmoSys server
    if csys_use:
      for k in csys_issues_created.keys():
        # We have the csys key, 
        thisnewnode = csys_issues_created[k]
        # and the normalized new node, which already has been updated
        # We have to look for the aliases
        for alias_path in inverse_aliases[thisnewnode['globalpath']]:
          # We will update the node where it was supposed to be the csID
          n = graphml_csid_nodes_fileid[alias_path]
          n.contents[0].replace_with(thisnewnode['csID'])
          # updating rmid
          n = graphml_rmid_nodes_fileid[alias_path]
          n.contents[0].replace_with(str(thisnewnode['rmid']))
          # updating url
          n = graphml_url_nodes_fileid[alias_path]
          n.contents[0].replace_with(thisnewnode['url'])
          # updating project
          n = graphml_project_nodes_fileid[alias_path]
          n.contents[0].replace_with(thisnewnode['project'])


      # Let's update the files
    for fn in filesoups.keys():
      with open(os.path.join(dirname,fn+'.graphml.out'), "w", encoding='utf-8') as file:
        file.write(str(filesoups[fn]))

    rows = [['RM#','url','RMID','ID','row#','subject','','tracker','Rlv?','status','parent', 
    'blocking_items','precedent_items','prMin','prDefault','prMax','prDefaultText','version','priority']]

    for key in normalized_dict.keys():
      row = []
      n = normalized_dict[key]

      strparent = ""
      if n['parentkey'] == None:
        if n['node_type'] == "prSys":
          if key in inverse_aliases.keys():
            if len(inverse_aliases[key]) > 0:
              n['parentkey'] = global_dict[inverse_aliases[key][0]]['parentkey']

      if n['parentkey']:
        strparent = node_aliases[n['parentkey']]
        if strparent in translator_dict.keys():
          strparent = translator_dict[strparent]

      s = ','
      strrel = ''
      if n['normalized_relations'] is not None:
        rels = []
        for r in n['normalized_relations']:
          if r in translator_dict.keys():
            rels += [translator_dict[r]]

          else:
            rels += [r]

        strrel = s.join(rels)

      strnext = ''
      if n['normalized_next'] is not None:
        rels = []
        for r in n['normalized_next']:
          if r in translator_dict.keys():
            rels += [translator_dict[r]]

          else:
            rels += [r]

        strnext = s.join(rels)

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

      #thisid = n['globalpath']
      if key in translator_dict.keys():
        thisid = translator_dict[key]

      else:
        thisid = key

      

      row += [[n['rmid'],n['url'],n['rmid'],thisid,'',n['name'],'',n['node_type'],'','',
        strparent,strrel,strnext,strmin,strdefault,strmax,strdefaulttext,'','Normal']]

      '''
      row += [[n['relations'],n['next'],n['default'],n['max']]]
      '''
      rows += row

    data.update({"Dict": [['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',5,'',len(rows)+1]
    , ['',''], ['',''], ['',global_file_identifier], ['',global_file_cscode]]})
    data.update({"Items": rows})
    data.update({"ExtraFields":[[]]})


    dirname = os.path.dirname(filename)
    basenamelist = os.path.splitext(os.path.basename(filename))
    onlyname = basenamelist[0]
    extension = basenamelist[1]
    odsextension = ".ods"
    
    save_data(os.path.join(dirname,deviceName+odsextension), data)




######### WE WILL PARSE THE COMMAND LINE ARGUMENTS FOR THE WRAPPER GEN #############
parser = argparse.ArgumentParser(description='Launches a PORIS device generation ODS from an GraphML diagrams directory describing the PORIS instrument')

## The second argument is the api ODS file
parser.add_argument('sys_dir',type=pathlib.Path, help="the path of a directory containing the PORIS instrument diagram")

# Obtaining the arguments from the command line
args=parser.parse_args()

# Printing the obtained arguments:
print("/* The PORIS instrument diagram directory is:",args.sys_dir.name+" */")
deviceName = pathlib.Path(args.sys_dir.name).stem
print("Device name:",deviceName)

# As an example of a constant defined in the configuration file, we'll print the welcome message
print(config.welcome_message)

create_tree_from_graphml_dir('models/'+args.sys_dir.name,deviceName)
