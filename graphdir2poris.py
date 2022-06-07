# Note, thanks to https://github.com/viperior/graphml-interpreter
import argparse
from locale import normalize                     # This library allows us to easily parse the command line arguments
import pathlib

import csv, os, re
from bs4 import BeautifulSoup
from pyexcel_ods import save_data
from collections import OrderedDict
from config_rm import *

# Importing test configuration file
import config
from graph2porislib import *
import glob

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

    #print("csCode:",file_cscode)
    #print("identifier:",file_identifier)

    # Create the local tree
    filterednodes = []
    print(len(groups),len(nodes))

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
      for n in node_data:
        if n['key']==csidkey:
          if len(n.contents) >= 1:
            thiscontent = n.contents[0].strip()
            if len(thiscontent) > 0:
              normal_node['csID'] = thiscontent

        if n['key']==urlkey:
          if len(n.contents) >= 1:
            thiscontent = n.contents[0].strip()
            if len(thiscontent) > 0:                
              normal_node['url'] = thiscontent

        if n['key']==csrmid:
          if len(n.contents) >= 1:
            thiscontent = n.contents[0].strip()
            if len(thiscontent) > 0:
              normal_node['rmid'] = thiscontent

        if n['key']==csproject:
          if len(n.contents) >= 1:
            thiscontent = n.contents[0].strip()
            if len(thiscontent) > 0:            
              normal_node['project'] = thiscontent
              if normal_node['project'] != basefilename:
                normal_node['external'] = True


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

      nodes_dict[normal_node['nodeid']] = normal_node
      global_dict[normal_node['globalid']] = normal_node

    # At this point we have the nodes for the current file
    # Let's calculate their paths
    for key in nodes_dict.keys():
      normal_node = nodes_dict[key]
      print(normal_node['globalid'])
      normal_node['nodepath'] = basefilename + '/' + create_local_path(nodes_dict,key)
      normal_node['globalpath'] = normal_node['project'] + '/' + create_global_path(nodes_dict,key,normal_node['project'])
      '''
      file_node = {}
      file_node['fileident'] = normal_node['nodeid']
      file_node['parentkey'] = normal_node['node_group_id']
      file_node['name'] = normal_node['node_name']
      localtree_key = basefilename + '/' +key
        
      global_dict[localtree_key] = file_node
      if normal_node['project'] == basefilename:
        normalized_key = localtree_key
        normalized_dict[normalized_key] = file_node
      '''

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


  import json
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
    print(key)
    print(node_aliases[key])
    normalized_node = normalized_dict[node_aliases[key]]
    for r in normal_node['relations']:
      normalized_node['normalized_relations'] += [node_aliases[r]]

    for r in normal_node['next']:
      normalized_node['normalized_next'] += [node_aliases[r]]

  out_file = open("global_dict.json", "w")
  json.dump(global_dict, out_file, indent=4)
  out_file.close()



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

    print(n['parentkey'])
    if n['parentkey']:
      strparent = node_aliases[n['parentkey']]

    s = ','
    strrel = ''
    if n['normalized_relations'] is not None:
      strrel = s.join(n['normalized_relations'])

    strnext = ''
    if n['normalized_next'] is not None:
      strnext = s.join(n['normalized_next'])

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

    thisid = n['globalpath']
     

    row += [[n['rmid'],n['url'],n['rmid'],thisid,'',n['name'],'',n['node_type'],'','',
      strparent,strrel,strnext,strmin,strdefault,strmax,strdefaulttext,'','Normal']]

    '''
    row += [[n['relations'],n['next'],n['default'],n['max']]]
    '''
    rows += row

  data.update({"Dict": [['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',5,'',len(rows)+1]
  , ['',''], ['',''], ['',file_identifier], ['',file_cscode]]})
  data.update({"Items": rows})
  data.update({"ExtraFields":[[]]})


  dirname = os.path.dirname(filename)
  basenamelist = os.path.splitext(os.path.basename(filename))
  onlyname = basenamelist[0]
  extension = basenamelist[1]
  odsextension = ".ods"
    

  save_data(os.path.join(dirname,onlyname+odsextension), data)




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
