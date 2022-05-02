# Note, thanks to https://github.com/viperior/graphml-interpreter
import argparse                     # This library allows us to easily parse the command line arguments

import csv, os, re
from bs4 import BeautifulSoup
from pyexcel_ods import save_data
from collections import OrderedDict
from pathlib import Path

# Importing test configuration file
import config


file_data = ['','']

def convert_list_to_string(list, delimiter):
  list_string = ''

  if len(list)>0:
    for item in list[:-1]:
      list_string = list_string + item + delimiter

    list_string = list_string + list[-1]

  return list_string

def convert_sorted_list_to_dictionary_with_sequence_index(list):
  dictionary_with_sequence_index = {}

  for index, value in enumerate(list):
    dictionary_with_sequence_index[value] = index + 1

  return dictionary_with_sequence_index

def create_ods_file_from_graphml_file(filename, deviceName):
  global file_data

  with open(filename) as file:
    soup = BeautifulSoup(file, 'lxml-xml')
    graph = soup.find("graph",{"id":"G"})
    nodes = soup.findAll("node", {"yfiles.foldertype":""})
    groups = soup.find_all("node", {"yfiles.foldertype":"group"})
    edges = soup.findAll("edge")

  # Retrieving file_data
  file_data = graph.find_all('data')
  file_cscode = ""
  file_identifier = ""
  for n in file_data:
    if n['key'] == "d1":
      file_cscode = n.contents[0]
    
    if n['key'] == "d2":
      file_identifier = n.contents[0]

  print("csCode:",file_cscode)
  print("identifier:",file_identifier)

  # First we must find the roots

  roots = []
  groups_dict = {}
  csv_dict_data = []

  for group in groups:
    group_dict = {}
    group_dict['min'] = None
    group_dict['default'] = None
    group_dict['max'] = None        
    group_dict['group_id'] = group['id']
    group_name = group.find('y:NodeLabel').text.strip()
    group_data = group.find_all('data')
    print("+++",group_name)
    for n in group_data:
      if n['key']!='d6':
        print("***",group_name,n.contents)
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

  nodes_dict = {}

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
    node_data = node.find_all('data')
    node_dict['min'] = None
    node_dict['default'] = None
    node_dict['max'] = None
    node_dict['defaulttext'] = None
    node_dict['relations'] = []
    node_dict['next'] = []
    node_shape = node.find('y:Shape')['type'].strip()
    print(node_dict['node_name'],node_shape)
    for n in node_data:
      if n['key']=='d6':
        node_dict['csID'] = n.contents[0]

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
            valueslist = second_label.split('<')
            print(">>>>>>",valueslist)
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
    csv_dict_data.append(node_dict)


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
    node_dict['relations'] = []
    node_dict['next'] = []
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
  
  rows = [['RM#','link','RMID','ID','row#','subject','description','tracker','Rlv?','status','parent',
  'blocking_items','precedent_items','prMin','prDefault','prMax','prDefaultText','version','priority']]
  for n in csv_dict_data:
    row = []
    n['node_id'] = n['node_id'].replace(':','')
    if n['node_group_id'] is not None:
      n['node_group_id'] = n['node_group_id'].replace(':','')

    relstr = ""
    first = True
    for c in n['relations']:
      if not first:
        relstr += ", "
      else:
        first = False
      
      relstr += c.replace(':','')

    n['relations'] = relstr

    relstr = ""
    first = True
    for c in n['next']:
      if not first:
        relstr += ", "
      else:
        first = False
      
      relstr += c.replace(':','')
    
    n['next'] = relstr

    strparent = ''
    if n['node_group_id'] is not None:
      strparent = n['node_group_id']

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

    row += [['','','',n['node_id'],'',n['node_name'],'',n['node_type'],'','',
      strparent,strrel,strnext,strmin,strdefault,strmax,strdefaulttext,'','Normal']]

    '''
    row += [[n['relations'],n['next'],n['default'],n['max']]]
    '''
    rows += row

  data.update({"Dict": [['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',5,'',len(csv_dict_data)+1]
  , ['',''], ['',''], ['',file_identifier], ['',file_cscode]]})
  data.update({"Items": rows})
  data.update({"ExtraFields":[[]]})
  save_data("./"+deviceName+".ods", data)

def get_filenames_in_directory(directory):
  filenames = []
  for root, dirs, files in os.walk(directory):
    for filename in files:
      filenames.append(filename)

  return filenames


######### WE WILL PARSE THE COMMAND LINE ARGUMENTS FOR THE WRAPPER GEN #############
parser = argparse.ArgumentParser(description='Launches a PORIS device generation ODS from an GraphML diagram describing the PORIS instrument')

## The second argument is the api ODS file
parser.add_argument('sys_file',type=argparse.FileType('r'), help="the path of a file containing the PORIS instrument diagram")

# Obtaining the arguments from the command line
args=parser.parse_args()

# Printing the obtained arguments:
print("/* The PORIS instrument diagram filename is:",args.sys_file.name+" */")
deviceName = Path(args.sys_file.name).stem
print("Device name:",deviceName)

# As an example of a constant defined in the configuration file, we'll print the welcome message
print(config.welcome_message)

create_ods_file_from_graphml_file(args.sys_file.name,deviceName)
