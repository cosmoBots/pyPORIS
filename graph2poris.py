# Note, thanks to https://github.com/viperior/graphml-interpreter

import csv, os, re
from bs4 import BeautifulSoup
from pyexcel_ods import save_data
from collections import OrderedDict

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

def create_csv_file_from_graphml_file(filename, source_directory, target_directory):
  global file_data
  data_file_full_path = source_directory + filename + '.graphml'

  with open(data_file_full_path) as file:
    soup = BeautifulSoup(file, 'lxml-xml')
    nodes = soup.findAll("node", {"yfiles.foldertype":""})
    groups = soup.find_all("node", {"yfiles.foldertype":"group"})
    edges = soup.findAll("edge")


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
    notenode = node.find('y:UMLNoteNode')
    if notenode is not None:
      file_data_str = node.find('y:NodeLabel').text.strip()
      file_data = file_data_str.split()
    
    else:    
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
      node_dict['relations'] = []
      node_dict['next'] = []
      node_shape = node.find('y:Shape')['type'].strip()
      print(node_dict['node_name'],node_shape)
      for n in node_data:
        if n['key']!='d6':
          print("***",node_dict['node_name'],n.contents)
          for c in n.contents:
            cs = c.split('\n')
            print("->",cs)
            for d in cs:
              e = d.split(':')
              print("!",e)
              if e[0] == 'csID':
                node_dict['csID'] = e[1]

      color_attribute = node.find('y:Fill')
      node_color = None
      if color_attribute is not None:
        if color_attribute.get('color') is not None:
          node_color = color_attribute['color'].strip()

      if node_shape == "parallelogram":
        if node_color is not None and node_color == "#99CCFF":
          node_dict['node_type'] = "prValue"
        
        else:
          node_dict['node_type'] = "prValueText"

      else:
        if node_shape == "roundrectangle":
          node_dict['node_type'] = "prMode"

        else:
          if node_color is not None:
            ischild = True
            node_dict['node_type'] = "prDataDouble"
            if node_color == "#FFFF00":
              node_dict['min'] = node_dict['node_name']
              print("min",node_dict['node_name'])
              groups_dict[node_dict['node_group_id']]['min'] = node_dict['node_name']

            else:
              if node_color == "#CC99FF":
                node_dict['default'] = node_dict['node_name']
                print("default",node_dict['default'])
                groups_dict[node_dict['node_group_id']]['default'] = node_dict['node_name']

              else:
                node_dict['max'] = node_dict['node_name']
                print("max",node_dict['max'])
                groups_dict[node_dict['node_group_id']]['max'] = node_dict['node_name']

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
      if not(ischild):
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

    '''
    strdefaulttext = ''
    if n['defaulttext'] is not None:
      strdefaulttext = n['defaulttext']
    '''

    row += [['','','',n['node_id'],'',n['node_name'],'',n['node_type'],'','',
    strparent,strrel,strnext,strmin,strdefault,strmax]]


    '''
    row += [[n['relations'],n['next'],n['default'],n['max']]]
    '''
    rows += row

  data.update({"Dict": [['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',5,'',len(csv_dict_data)+1]
  , ['',''], ['',''], ['',file_data[0]], ['',file_data[1]]]})
  data.update({"Items": rows})
  data.update({"ExtraFields":[[]]})
  save_data(target_directory+filename+".ods", data)


  csv_columns = [
    'node_id',
    'node_name',
    'node_group_id',
    'node_group_name',
    'node_type',
    'min',
    'default',
    'max',
    'relations',
    'next'
    #'node_group_sort_order'
  ]

  dict_data = csv_dict_data
  csv_filename = filename + '.csv'
  csv_file = target_directory + csv_filename

  try:
    with open(csv_file, 'w', newline='') as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
      writer.writeheader()
      for data in dict_data:
        writer.writerow(data)
  except IOError:
    print('I/O error')


def get_filenames_in_directory(directory):
  filenames = []
  for root, dirs, files in os.walk(directory):
    for filename in files:
      filenames.append(filename)

  return filenames

def graphml_interpreter():
  source_directory = './graphml/'
  target_directory = './'
  filenames = get_filenames_in_directory(source_directory)

  for file in filenames:
    filename = file.replace('.graphml', '')
    create_csv_file_from_graphml_file(filename, source_directory, target_directory)

graphml_interpreter()
