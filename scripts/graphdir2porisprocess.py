# Note, thanks to https://github.com/viperior/graphml-interpreter
import csv, os, re
from bs4 import BeautifulSoup
from pyexcel_ods import save_data
from collections import OrderedDict
from config_csys import *
from pathlib import Path

# Importing test configuration file
import config
from graph2porislib import *
from poris_codegen import build_nodes_tree, createPythonCode
import glob

import json
from cosmosys_api import CosmosysApi

debug_json_dir = Path("tmp") / "poris-debug"

def write_debug_json(filename, payload):
  debug_json_dir.mkdir(parents=True, exist_ok=True)
  with open(debug_json_dir / filename, "w") as out_file:
    json.dump(payload, out_file, indent=4)

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
  print("create local path for",key)
  n = ndict[key]
  path = gettypeabbrev(n['node_type'])+n['name']
  if 'node_group_id' in n.keys():
    if len(n['node_group_id'])>0:
      path = create_local_path(ndict,n['node_group_id']) + '/' + path
      print(path)

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

    print(path)
    return path

  else:
    return None

def create_tree_from_graphml_dir(dirname, deviceName, emit_ods=True, emit_python=True, python_output_dir=None, ods_output_dir=None, root_name=None, debug_json=False):
  #print(dirname+'/*.graphml')
  filenames = glob.glob(dirname+'/*.graphml')
  #filenames = glob.glob(dirname+'/*')
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
  filesoups = {}
  if root_name is None:
    root_name = deviceName
  
  if csys_use:
    continueProcess = False

    from redminelib import Redmine

    if csys_ignorecert:
        cosmosys = Redmine(csys_server_url,key=csys_key_txt, requests={'verify': False})
        csys_api = CosmosysApi(csys_server_url, csys_key_txt, verify=False)
    else:
        cosmosys = Redmine(csys_server_url,key=csys_key_txt)
        csys_api = CosmosysApi(csys_server_url, csys_key_txt)

    trackerdict = {}
    trackers = cosmosys.tracker.all()
    for tr in trackers:
        trackerdict[tr.name] = tr


    projects = cosmosys.project.all()

    csys_projects = {}
    csys_issues = {}
    csys_prj_dict = {}
    csys_issues_created = {}

    print("Projects:")
    for p in projects:
        print("    ",p.identifier,"     | ",p.name)
        csys_prj_dict[p.identifier] = p
        if p.identifier == root_name:
          continueProcess = True

    if continueProcess:
      continueProcess = False
      rootproject = cosmosys.project.get(root_name)
      if rootproject is None:
        print("We can not obtain the root project for this GraphML folder")
      else:
        print ("Root project found at cosmoSys server: ",rootproject.identifier," | ",rootproject.name)
        continueProcess = True
        csys_projects[root_name] = rootproject


  if continueProcess:
    for filename in filenames:
      basefilename = Path(filename).stem
      print("---------------------",basefilename,"------------------------------")
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
      print("csid key",csidkey)
      print("rmid key",csrmid)

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

      if root_name == basefilename:
        global_file_identifier = file_identifier
        global_file_cscode = file_cscode
      
      #print("csCode:",file_cscode)
      #print("identifier:",file_identifier)

      # Create the local tree
      groups_dict = {}

      for group in groups:
        #print(group)
        group_node = {}
        group_node['group_id'] = group['id']
        group_node['group_name'] = group.find('y:NodeLabel').text.strip()
        group_id_parts = re.findall(r'n\d{1,}', group_node['group_id'])

        if(len(group_id_parts) > 1):
          group_node['parent_group_id'] = convert_list_to_string(group_id_parts[:-1], '::')
          #print(group_node)
          #print(group_id_parts)
          #print(group_node['parent_group_id'])
          group_node['parent_group_name'] = groups_dict[group_node['parent_group_id']]['group_name']

        groups_dict[group_node['group_id']] = group_node

      nodes_dict = {}

      for node in nodes + groups:
        normal_node = {}
        normal_node['nodeid'] = node['id']
        nodeid_parts = re.findall(r'n\d{1,}', normal_node['nodeid'])
        normal_node['node_group_id'] = convert_list_to_string(nodeid_parts[:-1], '::')
        normal_node['name'] = node.find('y:NodeLabel').text.strip()
        print("**********",normal_node['name'])

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
        normal_node['rmid'] = ""
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
                normal_node['rmid'] = int(thiscontent)

          if n['key']==csproject:
            projectdatanode = n
            if len(n.contents) >= 1:
              thiscontent = n.contents[0].strip()
              if len(thiscontent) > 0:
                print("Uno",normal_node['name'],thiscontent)
                normal_node['project'] = thiscontent
                if normal_node['project'] != file_identifier:
                  normal_node['external'] = True

        if csiddatanode is None:
          csiddatanode = soup.new_tag('data',key=csidkey)
          csiddatanode.string = ""
          node.append(csiddatanode)
        
        if rmiddatanode is None:
          rmiddatanode = soup.new_tag('data',key=csrmid)
          rmiddatanode.string = "0"
          node.append(rmiddatanode)

        if urldatanode is None:
          urldatanode = soup.new_tag('data',key=urlkey)
          urldatanode.string = "bla"
          node.append(urldatanode)

        if projectdatanode is None:
          projectdatanode = soup.new_tag('data',key=csproject)
          projectdatanode.string = ""
          node.append(projectdatanode)
          print("Creo el projectdatanode para",normal_node['name'])

        graphml_csid_nodes_fileid[normal_node['globalid']] = csiddatanode
        graphml_url_nodes_fileid[normal_node['globalid']] = urldatanode
        graphml_rmid_nodes_fileid[normal_node['globalid']] = rmiddatanode
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
          if normal_node['project'] not in csys_prj_dict:
            print("Error, the node has a project identifier which is not present in the cosmoSys server")
            return None

          if normal_node['csID'] is not None and normal_node['csID'] not in csys_issues:
            item_data = csys_api.by_csid(root_name, normal_node['csID'])
            if item_data is not None:
              if item_data['project']['identifier'] != normal_node['project']:
                print("Error, CSID", normal_node['csID'], "belongs to project", item_data['project']['identifier'], "not", normal_node['project'])
                return None
              issue = cosmosys.issue.get(item_data['id'])
              csys_projects[normal_node['project']] = csys_prj_dict[normal_node['project']]
              csys_issues[normal_node['csID']] = {'csys': issue, 'nodes': [normal_node]}
            else:
              # A legacy/source CSID is not a native identity in this cosmoSys tree.
              normal_node['csID'] = None

          if normal_node['csID'] is None:
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
              item_data = csys_api.by_id(root_name, thisCsysIss.id)
              if item_data is None:
                raise RuntimeError(f"cosmoSys created issue {thisCsysIss.id} but returned no native CSID")
              thisCsysIss = cosmosys.issue.get(thisCsysIss.id)
              thisCsId = item_data['csid']
              normal_node['csID'] = thisCsId
              normal_node['rmid'] = thisCsysIss.id
              normal_node['url'] = url
              csys_issues_created[thisCsId] = normal_node
              csys_issues[thisCsId] = {'csys': thisCsysIss, 'nodes': [normal_node]}
              # We will update the node where it was supposed to be the csID
              n = graphml_csid_nodes_fileid[normal_node['globalid']]
              n.contents[0].replace_with(normal_node['csID'])
              # updating rmid
              n = graphml_rmid_nodes_fileid[normal_node['globalid']]
              if len(n.contents) >= 1:
                n.contents[0].replace_with(str(normal_node['rmid']))
              
              else:
                n.insert(0,str(normal_node['rmid']))

              # updating url
              n = graphml_url_nodes_fileid[normal_node['globalid']]
              if len(n.contents) >= 1:
                n.contents[0].replace_with(normal_node['url'])
              
              else:
                n.insert(0,normal_node['url'])

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
        print("normalmode['project']",normal_node['project'])
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
    print("--------------------------- FILES ALREADY PARSED -----------------------------")

    if debug_json:
      write_debug_json("node_aliases.json", node_aliases)
      write_debug_json("inverse_aliases.json", inverse_aliases)
      write_debug_json("normalized_dict.json", normalized_dict)
      write_debug_json("global_dict.json", global_dict)

    # And now, we have to re-link the relationships to the normalized targets
    for key in global_dict:
      print("normalize relationships of",key)
      normal_node = global_dict[key]
      #print("normal_mode",normal_node)
      #print("alias",node_aliases[key])
      normalized_node = normalized_dict[node_aliases[key]]
      #print("normalized_node",normalized_node)
      for r in normal_node['relations']:
        normalized_node['normalized_relations'] += [node_aliases[r]]

      for r in normal_node['next']:
        normalized_node['normalized_next'] += [node_aliases[r]]

    print("End loop")
    if debug_json:
      write_debug_json("global_dict2.json", global_dict)

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
        if thisnewnode['globalpath'] in inverse_aliases.keys():
          for alias_path in inverse_aliases[thisnewnode['globalpath']]:
            # We will update the node where it was supposed to be the csID
            n = graphml_csid_nodes_fileid[alias_path]
            n.contents[0].replace_with(thisnewnode['csID'])
            # updating rmid
            n = graphml_rmid_nodes_fileid[alias_path]
            if len(n.contents) >= 1:
              n.contents[0].replace_with(str(thisnewnode['rmid']))
            
            else:
              n.insert(0,str(thisnewnode['rmid']))

            # updating url
            n = graphml_url_nodes_fileid[alias_path]
            if len(n.contents) >= 1:
              n.contents[0].replace_with(thisnewnode['url'])
            
            else:
              n.insert(0,thisnewnode['url'])

            # updating project
            n = graphml_project_nodes_fileid[alias_path]
            n.contents[0].replace_with(thisnewnode['project'])

      # Synchronize canonical hierarchy and activation edges after all files
      # and external aliases have been normalized.  External replicas remain
      # aliases; only the canonical item receives parent/relationship updates.
      for key, node in normalized_dict.items():
        if node['parentkey'] is None and node['node_type'] == 'prSys' and inverse_aliases.get(key):
          node['parentkey'] = global_dict[inverse_aliases[key][0]]['parentkey']

        child_entry = csys_issues.get(node['csID'])
        if child_entry is None:
          continue
        child_issue = child_entry['csys']

        poris_attributes = {}
        if node['node_type'] == 'prValFloat':
          poris_attributes['pr_value_kind'] = 'float'
          for source_name, api_name in [('min', 'pr_min'), ('default', 'pr_default'), ('max', 'pr_max')]:
            if node.get(source_name) is not None:
              poris_attributes[api_name] = node[source_name]
        elif node['node_type'] == 'prValText':
          poris_attributes['pr_value_kind'] = 'text'
          if node.get('defaulttext') is not None:
            poris_attributes['pr_default_text'] = node['defaulttext']
        elif node['node_type'] == 'prValue':
          poris_attributes['pr_value_kind'] = 'enum'
        if poris_attributes:
          csys_api.update_by_id(root_name, child_issue.id, poris_attributes)

        parent_key = node.get('parentkey')
        if parent_key:
          parent_path = node_aliases.get(parent_key, parent_key)
          parent_node = normalized_dict.get(parent_path)
          parent_entry = csys_issues.get(parent_node['csID']) if parent_node else None
          if parent_entry is None:
            raise RuntimeError(f"Cannot resolve canonical parent for {node['name']} ({node['csID']})")
          parent_issue = parent_entry['csys']
          current_parent = getattr(child_issue, 'parent', None)
          current_parent_id = getattr(current_parent, 'id', None)
          if current_parent_id != parent_issue.id:
            cosmosys.issue.update(child_issue.id, parent_issue_id=parent_issue.id)
            child_issue = cosmosys.issue.get(child_issue.id)
            child_entry['csys'] = child_issue

        for target_path in node.get('normalized_relations', []):
          target_node = normalized_dict.get(target_path)
          target_entry = csys_issues.get(target_node['csID']) if target_node else None
          if target_entry is None:
            raise RuntimeError(f"Cannot resolve canonical PORIS relation target {target_path}")
          target_issue = target_entry['csys']
          existing = cosmosys.issue_relation.filter(issue_id=target_issue.id)
          already_linked = any(
            relation.relation_type == 'precedes' and
            relation.issue_id == target_issue.id and relation.issue_to_id == child_issue.id
            for relation in existing
          )
          if not already_linked:
            cosmosys.issue_relation.create(
              issue_id=target_issue.id,
              issue_to_id=child_issue.id,
              relation_type='precedes',
              delay=0
            )


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
    if emit_ods:
      ods_dir = ods_output_dir if ods_output_dir is not None else dirname
      os.makedirs(ods_dir, exist_ok=True)
      save_data(os.path.join(ods_dir, deviceName + odsextension), data)

    if emit_python:
      python_nodes = {}
      for key, n in normalized_dict.items():
        ident = translator_dict.get(key, key)
        # parentkey stores the globalid of the parent group; convert it to globalpath via node_aliases, then to ident
        parent_key = n.get('parentkey') or n.get('parent')
        parent_ident = None
        if parent_key:
          parent_path = node_aliases.get(parent_key, parent_key)
          parent_ident = translator_dict.get(parent_path, parent_path)
        rels = []
        rel_sources = n.get('normalized_relations', n.get('relations', [])) or []
        for rel in rel_sources:
          if rel in translator_dict:
            rels.append(translator_dict[rel])
          else:
            rels.append(rel)

        nexts = []
        next_sources = n.get('normalized_next', n.get('next', [])) or []
        for rel in next_sources:
          if rel in translator_dict:
            nexts.append(translator_dict[rel])
          else:
            nexts.append(rel)

        python_nodes[ident] = {
          'ident': ident,
          'id': n['rmid'] if n['rmid'] is not None else ident,
          'subject': n['name'],
          'description': n['defaulttext'] if n['defaulttext'] is not None else "",
          'parent': parent_ident,
          'tracker': n['node_type'],
          'blocking': rels,
          'precedents': nexts,
          'min': n['min'],
          'default_data': n['default'],
          'max': n['max'],
          'deftext': n['defaulttext'],
          'children': [],
          'virtual': False
        }

      python_tree = build_nodes_tree(python_nodes)
      createPythonCode(python_tree, deviceName, python_output_dir if python_output_dir is not None else dirname, "")
