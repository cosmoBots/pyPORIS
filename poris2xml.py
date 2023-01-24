# Importing auxiliar libraries for the test
import argparse                     # This library allows us to easily parse the command line arguments

from pyexcel_ods import get_data    # This function allows us to easily read an ODS file (for api)
from xml.dom import minidom
from pathlib import Path
import os

# Importing test configuration file
import config

def nametoidl(n):
    ret = n.replace('(','_')
    ret = ret.replace(')','_')
    ret = ret.replace('.','_')
    ret = ret.replace('+','p')
    ret = ret.replace('/','_')
    ret = ret.replace('¿','_')    
    ret = ret.replace('?','_')    
    ret = ret.replace('á','a')
    ret = ret.replace('é','e')
    ret = ret.replace('í','i')
    ret = ret.replace('ó','o')
    ret = ret.replace('ú','u')
    ret = ret.replace('Á','A')
    ret = ret.replace('É','E')
    ret = ret.replace('Í','I')
    ret = ret.replace('Ó','O')
    ret = ret.replace('Ú','U')
    ret = ret.replace('ñ','ny')
    ret = ret.replace('Ñ','NY')
    
    if (ret.lower() == 'sequence'):
        ret = ret+"b"
    

    return ret

def desctomonit(n):
    return nametoidl(n.split('\n')[0].split('\r')[0])

def replaceStringFile(pattern_file,dest_file,pattern_text, replacement_text):
    # Read in the file
    with open(pattern_file, 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(pattern_text, replacement_text)
    # Write the file out again
    with open(dest_file, 'w') as file:
        file.write(filedata)    

def fileGenFromPattern(pattern_file_str,src_file_str, dest_file_str,marker_str,particles_dir,replacement_dir):

    # Loading the capsule declaration pattern
    pattern_lines = []
    with open(pattern_file_str, 'r') as pattern_file:
        pattern_lines = pattern_file.readlines()

    # Computing the capsule declaration lines
    lines_to_include = []

    particle_lines = {}
    
    for k in particles_dir.keys():
        for v in particles_dir[k]:
            particle_lines[v] = []
        
    
    for l in pattern_lines:
        # We replace the constant part
        line_base = l
        for k2 in replacement_dir.keys():
            line_base = line_base.replace(k2,replacement_dir[k2])

        # We iterate creating lines for each particle
        for k in particles_dir.keys():
            for v in particles_dir[k]:
                line_to_include = line_base.replace(k,v)
                particle_lines[v] += [line_to_include]


    for k in particle_lines.keys():
        lines_to_include += particle_lines[k]
        lines_to_include += ["\n"]


    filesrc = open(src_file_str, 'r')
    filedest = open(dest_file_str, 'w')

    for line in filesrc:
        filedest.write(line)
        if marker_str in line:
            filedest.writelines(lines_to_include)

    filesrc.close()
    filedest.close()    



######### WE WILL PARSE THE COMMAND LINE ARGUMENTS FOR THE WRAPPER GEN #############
parser = argparse.ArgumentParser(description='Launches a PORIS device generation from an ODS file describing the PORIS instrument')

## The second argument is the api ODS file
parser.add_argument('sys_file',type=argparse.FileType('r'), help="the path of a file containing the PORIS instrument description")

# Obtaining the arguments from the command line
args=parser.parse_args()

# Printing the obtained arguments:
print("/* The PORIS instrument description ODS filename is:",args.sys_file.name+" */")
deviceName = Path(args.sys_file.name).stem
print("Device name:",deviceName)

# As an example of a constant defined in the configuration file, we'll print the welcome message
print(config.welcome_message)

def loadODS():

    dictdata = get_data(args.sys_file.name,start_row=config.dict_max_rows_row, row_limit=config.dict_max_rows_row+1, 
        start_column=config.dict_max_rows_column,column_limit=config.dict_max_rows_column)[config.dict_file_sheet]

    desc_file_row_limit = dictdata[0][1]
    # Now we read the PORIS instrument description from the file file
    filedata = get_data(args.sys_file.name,start_row=config.desc_file_start_row, row_limit=desc_file_row_limit, 
        start_column=config.desc_file_start_column,column_limit=config.desc_file_column_limit)
    nodesdata = filedata[config.desc_file_sheet]

    virtual_nodes_counter = 1

    nodes_dict = {}
    virtual_nodes = {}
    rowcount = 0

    for row in nodesdata:
        if (len(row)>1):
            rowcount += 1
            print("row",row)
            thiskey = row[config.desc_ident_column]
            if (len(thiskey)>0):
                # print(thiskey)

                thisnode = {}
                thisnode['ident'] = thiskey
                # In case we came from graphml, this column could be empty
                thisid = str(row[config.desc_id_column])
                if len(thisid) <= 0:
                    # TODO: Find a more robust strategy to generate identifiers 
                    # out of the Redmine space
                    thisid = 2000000000+rowcount

                thisnode['id'] = thisid
                thisnode['subject'] = row[config.desc_subject_column]
                thisnode['description'] = row[config.desc_description_column]
                thisnode['parent'] = row[config.desc_parent_column]
                blockingstr = row[config.desc_blocking_column]
                thisnode['tracker'] = row[config.desc_tracker_column]
                thisnode['blocking'] = []
                thisnode['virtual'] = False
                if blockingstr is not None and len(blockingstr)>0:
                    thisnode['blocking'] = [x.strip() for x in blockingstr.split(',')]
                else:
                    if thisnode['tracker'] == "prMode":
                        # The mode can not hold no destinations because the player will show an empty slot,
                        # we will create a virtual value for it
                        virtnode = {}
                        virtid = str(-virtual_nodes_counter)
                        virtual_nodes_counter += 1
                        virtident = "VIRT"+virtid
                        virtnode['ident'] = virtident
                        virtnode['id'] = virtid
                        virtnode['tracker'] = "prValue"
                        virtnode['subject'] = thisnode['subject']
                        virtnode['description'] = thisnode['description']
                        virtnode['parent'] = thisnode['parent']
                        virtnode['blocking'] = []
                        virtnode['precedents'] = []
                        virtnode['children'] = []
                        virtnode['virtual'] = True
                        nodes_dict[virtident] = virtnode
                        thisnode['blocking'] = [virtident]
                        
                    else:
                        thisnode['blocking'] = []

                # print("Parsed:",thisnode['blocking'])
                thisnode['min'] = row[config.desc_min_column]
                thisnode['default_data'] = row[config.desc_def_column]
                thisnode['max'] = row[config.desc_max_column]
                thisnode['deftext'] = row[config.desc_deftext_column]
                precedentstr = row[config.desc_precedents_column]
                thisnode['precedents'] = []
                if precedentstr is not None:
                    thisnode['precedents'] = [x.strip() for x in precedentstr.split(',')]
                    
                else:
                    thisnode['precedents'] = []

                thisnode['children'] = []
                nodes_dict[thiskey] = thisnode

    # Relationships
    for thiskey in nodes_dict.keys():
        thisnode = nodes_dict[thiskey]

        # Parent relationship
        if thisnode['parent'] is not None:
            parentkey = thisnode['parent']
            if len(parentkey) > 0:
                if parentkey in nodes_dict.keys():
                    thisparent = nodes_dict[parentkey]
                    thisnode['parentnode'] = thisparent
                    thisparent['children'].append(thiskey)

    # Create engineering modes
    nodes_to_add = {}
    for thiskey in nodes_dict.keys():
        thisnode = nodes_dict[thiskey]
        
        if thisnode['virtual'] == False:
            if thisnode['tracker'] == "prSys":
                # Now, for each node of type prSys we must
                # create a new mode, engineering
                virtnode = {}
                virtid = str(-virtual_nodes_counter)
                virtual_nodes_counter += 1
                virtident = "ENG"+virtid
                virtnode['ident'] = virtident
                virtnode['id'] = virtid
                virtnode['tracker'] = "prMode"
                virtnode['subject'] = "Engineering"
                virtnode['description'] = thisnode['subject']+" engineering mode"
                virtnode['parent'] = thiskey
                virtnode['parentnode'] = thisnode
                virtnode['blocking'] = []
                virtnode['precedents'] = []
                virtnode['children'] = []
                virtnode['virtual'] = False
                
                # The engineering mode will be blocked by all the modes of its children
                for ch0 in thisnode['children']:
                    if nodes_dict[ch0]['tracker'] == "prSys" or nodes_dict[ch0]['tracker'] == "prParam":
                        for ch in nodes_dict[ch0]['children']:
                            if ch in nodes_dict.keys():
                                if nodes_dict[ch]['tracker'] == "prMode":
                                    if nodes_dict[ch]['virtual'] == False:
                                        virtnode['blocking'] += [ch]
                                        #print(virtnode['blocking'])

                if len(virtnode['blocking']) > 0:
                    nodes_to_add[virtident] = virtnode
                    thisnode['children'].append(virtident)

    for n in nodes_to_add.keys():
        nodes_dict[n] = nodes_to_add[n]

    tree_dict = {}
    while len(tree_dict) < len(nodes_dict):
        for k in nodes_dict.keys():
            if k not in tree_dict.keys():
                if 'parentnode' not in nodes_dict[k].keys():
                    tree_dict[k] = nodes_dict[k]
                    print("Adding ROOT",tree_dict[k]['subject'])
                
                else:
                    if nodes_dict[k]['parent'] in tree_dict.keys():
                        tree_dict[k] = nodes_dict[k]
                        print("Adding NODE",tree_dict[k]['parentnode']['subject'],":",tree_dict[k]['subject'])

    for n in nodes_to_add.keys():
        # Tengo que añadir el bloqueo de los modos de ingeniería
        # hijos a los modos de ingeniería padres
        virtnode = nodes_to_add[n]
        thisparent = virtnode['parentnode']
        for c in thisparent['children']:
            if c != n and thisparent["tracker"] == "prSys":
                for c2 in tree_dict[c]['children']:
                    #print(c2,"va a",n,"?")
                    if c2 in nodes_to_add.keys():
                        print(c2,nodes_to_add[c2]['description'],"bloquea a",n,virtnode['description'])
                        virtnode['blocking'] += [c2]
                        #print(virtnode['blocking'])


    for n in nodes_to_add.keys():
        #print("Añado el nodo ",n)
        #print(nodes_to_add[n])
        tree_dict[n] = nodes_to_add[n]

    for k in tree_dict.keys():
        n = tree_dict[k]
        print(k,n['subject'])

    return tree_dict


# This function will create:
# - The instrument XML
def createPorisXML(nodes_dict,deviceName):

    rootInstr = minidom.Document()
    xmlInstr = rootInstr.createElement('sub-systems-v4')
    rootInstr.appendChild(xmlInstr)


    # XML generation: first step is dump the values
    for thiskey in nodes_dict.keys():
        thisnode = nodes_dict[thiskey]
        '''
        <value>
            <id type="integer">503</id>
            <name>Tx2.0</name>
            <node-type-id type="integer">5</node-type-id>
            <project-id type="integer">13</project-id>
            <type>Value</type>
            <value-formatter-id type="integer" nil="true"></value-formatter-id>
            <destinations type="array"/>
            <node-attributes type="array"/>
            <labels type="array">
            <label>
                <name>2.0 arcsecs</name>
                <scope-kind>node-type-id
                <name>OPMS</name>
                </scope-kind>
            </label>
            </labels>
        </value>
        <value-double-range>
            <id type="integer">518</id>
            <name>TxExpTimeRange</name>
            <node-type-id type="integer">5</node-type-id>
            <project-id type="integer">13</project-id>
            <default-float type="float">0.01</default-float>        
            <rangemax type="float">1000.0</rangemax>
            <rangemin type="float">0.0</rangemin>
            <type>ValueDoubleRange</type>
            <value-formatter-id type="integer">5</value-formatter-id>
            <destinations type="array"/>
            <node-attributes type="array"/>
            <labels type="array"/>
        </value-double-range>
    <value-string>
        <default-string>First Name</default-string>
        <id type="integer">602</id>
        <name>FirstNameString</name>
        <node-type-id type="integer">5</node-type-id>
        <project-id type="integer">17</project-id>
        <type>ValueString</type>
        <value-formatter-id type="integer" nil="true"></value-formatter-id>
        <node-attributes type="array"/>
        <destinations type="array"/>
        <labels type="array"/>
    </value-string>
        '''
        if thisnode['tracker'] == "prValue" or thisnode['tracker'] == "prValFloat" or thisnode['tracker'] == "prValText":

            if thisnode['tracker'] == "prValue":
                valueNode = rootInstr.createElement('value')
            else:
                if thisnode['tracker'] == "prValFloat":
                    valueNode = rootInstr.createElement('value-double-range')

                else:
                    if thisnode['tracker'] == "prValText":
                        valueNode = rootInstr.createElement('value-string')
                    else:
                        valueNode = rootInstr.createElement('Error!!!3')
                        print("Error3!")

            # common part
            # <id type="integer">503</id>
            idChild = rootInstr.createElement('id')
            idChild.setAttribute("type", "integer")
            valueText = rootInstr.createTextNode(str(thisnode['id']))
            idChild.appendChild(valueText)
            valueNode.appendChild(idChild)

            idChild = rootInstr.createElement('ident')
            valueText = rootInstr.createTextNode(thiskey)
            idChild.appendChild(valueText)
            valueNode.appendChild(idChild)

            # <name>Tx2.0</name>
            nameChild = rootInstr.createElement('name')
            valueText = rootInstr.createTextNode(nametoidl(str(thisnode['subject'])))
            nameChild.appendChild(valueText)
            valueNode.appendChild(nameChild)

            # <node-type-id type="integer">5</node-type-id>
            nodeTypeChild = rootInstr.createElement('node-type-id')
            nodeTypeChild.setAttribute("type", "integer")
            valueText = rootInstr.createTextNode("5")
            nodeTypeChild.appendChild(valueText)
            valueNode.appendChild(nodeTypeChild)

            # <project-id type="integer">13</project-id>
            projectIdChild = rootInstr.createElement('project-id')
            projectIdChild.setAttribute("type", "integer")
            valueText = rootInstr.createTextNode("13")
            projectIdChild.appendChild(valueText)
            valueNode.appendChild(projectIdChild)

            if thisnode['tracker'] == "prValue":
                # <type>Value</type>
                typeChild = rootInstr.createElement('type')
                valueText = rootInstr.createTextNode("Value")
                typeChild.appendChild(valueText)
                valueNode.appendChild(typeChild)            

                # <value-formatter-id type="integer" nil="true"></value-formatter-id>
                child = rootInstr.createElement('value-formatter-id')
                child.setAttribute("type", "integer")
                child.setAttribute("nil","true")
                valueNode.appendChild(child)

            else:
                if thisnode['tracker'] == "prValFloat":
                    # <type>ValueDoubleRange</type>
                    typeChild = rootInstr.createElement('type')
                    valueText = rootInstr.createTextNode("ValueDoubleRange")
                    typeChild.appendChild(valueText)
                    valueNode.appendChild(typeChild)

                    # <value-formatter-id type="integer">5</value-formatter-id>
                    child = rootInstr.createElement('value-formatter-id')
                    child.setAttribute("type", "integer")
                    valueText = rootInstr.createTextNode("5")
                    child.appendChild(valueText)
                    valueNode.appendChild(child)

                    min_data = str(thisnode['min'])
                    default_data = str(thisnode['default_data'])
                    max_data = str(thisnode['max'])

                    # <default-float type="float">0.01</default-float>
                    child = rootInstr.createElement('default-float')
                    child.setAttribute("type", "float")
                    valueText = rootInstr.createTextNode(default_data)
                    child.appendChild(valueText)
                    valueNode.appendChild(child)

                    # <rangemax type="float">1000.0</rangemax>
                    child = rootInstr.createElement('rangemax')
                    child.setAttribute("type", "float")
                    valueText = rootInstr.createTextNode(max_data)
                    child.appendChild(valueText)
                    valueNode.appendChild(child)

                    # <rangemin type="float">0.0</rangemin>
                    child = rootInstr.createElement('rangemin')
                    child.setAttribute("type", "float")
                    valueText = rootInstr.createTextNode(min_data)
                    child.appendChild(valueText)
                    valueNode.appendChild(child)

                else:
                    if thisnode['tracker'] == "prValText":
                        # <type>ValueString</type>
                        typeChild = rootInstr.createElement('type')
                        valueText = rootInstr.createTextNode("ValueString")
                        typeChild.appendChild(valueText)
                        valueNode.appendChild(typeChild)

                        # <value-formatter-id type="integer" nil="true"></value-formatter-id>
                        child = rootInstr.createElement('value-formatter-id')
                        child.setAttribute("type", "integer")
                        child.setAttribute("nil", "true")
                        valueNode.appendChild(child)

                        deftext = str(thisnode['deftext'])
                        # <default-string>First Name</default-string>
                        child = rootInstr.createElement('default-string')
                        valueText = rootInstr.createTextNode(deftext)
                        child.appendChild(valueText)
                        valueNode.appendChild(child)                                                  

            # <destinations type="array"/>
            child = rootInstr.createElement('destinations')
            child.setAttribute("type", "array")
            valueNode.appendChild(child)
            
            # <node-attributes type="array"/>
            child = rootInstr.createElement('node-attributes')
            child.setAttribute("type", "array")
            valueNode.appendChild(child)

            # <labels type="array">
            child = rootInstr.createElement('labels')
            child.setAttribute("type", "array")
            valueNode.appendChild(child)

            xmlInstr.appendChild(valueNode)

    sorted_nodes_dict = []
    pending_nodes_dict = list(nodes_dict.keys())

    # First we will add all the subsystems without children subsystems
    while len(sorted_nodes_dict) < len(nodes_dict):
        for nodekey in pending_nodes_dict:
            if nodekey not in sorted_nodes_dict:
                thisnode = nodes_dict[nodekey]
                includenode = True
                if thisnode['tracker'] == "prParam" or thisnode['tracker'] == "prSys":
                    #print("trying to include:",nodekey,thisnode['subject'],thisnode['tracker'])
                    for childkey in thisnode['children']:
                        if len(childkey)>0:
                            childlevel = nodes_dict[childkey]['tracker']
                            #print("child:",childkey,nodes_dict[childkey]['subject'],childlevel)
                            if childlevel == "prParam" or childlevel == "prSys":
                                if childkey not in sorted_nodes_dict:
                                    includenode = False
                                    print("oops!")

                else:
                    if thisnode['tracker'] == "prMode":
                        #print("trying to include:",nodekey,thisnode['subject'],thisnode['tracker'])
                        #print(thisnode['blocking'])
                        for childkey in thisnode['blocking']:
                            if len(childkey)>0:
                                print("childkey:",childkey)
                                # If exporting partial projects, the key should fail
                                if childkey in nodes_dict.keys():
                                    childlevel = nodes_dict[childkey]['tracker']
                                    #print("child:",childkey,nodes_dict[childkey]['subject'],childlevel)
                                    if childkey not in sorted_nodes_dict:
                                        includenode = False
                                        print("oops!")
                                    
                                else:
                                    print("The key",childkey,"is not found, maybe you are exporting a partial project?")
                    

                if includenode:
                    print("---> Including:",nodekey,nodes_dict[nodekey]['subject'],nodes_dict[nodekey]['tracker'])
                    sorted_nodes_dict.append(nodekey)
                else:
                    print("---> NOT INCLUDED",nodekey)

    # XML generation: second step is dump the modes
    for thiskey in sorted_nodes_dict:
        thisnode = nodes_dict[thiskey]
        '''
        <mode>
            <default-mode-id type="integer" nil="true"></default-mode-id>
            <default-value-id type="integer" nil="true"></default-value-id>

            <id type="integer">519</id>
            <name>TxMasksAll</name>
            <node-type-id type="integer">6</node-type-id>
            <project-id type="integer">13</project-id>
            <type>Mode</type>
            
            <destinations type="array">
            <destination type="Value">
                <id type="integer">504</id>
            </destination>
            <destination type="Value">
                <id type="integer">505</id>
            </destination>
            <destination type="Value">
                <id type="integer">503</id>
            </destination>
            </destinations>
            
            <node-attributes type="array"/>
            <labels type="array">
            <label>
                <name>All</name>
                <scope-kind>
                <name>OPMS</name>
                </scope-kind>
            </label>
            </labels>
        </mode>
        '''
        if thisnode['tracker'] == "prMode":
            modeNode = rootInstr.createElement('mode')

            # <default-mode-id type="integer" nil="true"></default-mode-id>
            idChild = rootInstr.createElement('default-mode-id')
            idChild.setAttribute("type", "integer")
            idChild.setAttribute("nil", "true")
            modeNode.appendChild(idChild)

            # <default-value-id type="integer" nil="true"></default-value-id>
            idChild = rootInstr.createElement('default-value-id')
            idChild.setAttribute("type", "integer")
            idChild.setAttribute("nil", "true")
            modeNode.appendChild(idChild)

            # <id type="integer">519</id>
            idChild = rootInstr.createElement('id')
            idChild.setAttribute("type", "integer")
            valueText = rootInstr.createTextNode(str(thisnode['id']))
            idChild.appendChild(valueText)
            modeNode.appendChild(idChild)

            idChild = rootInstr.createElement('ident')
            valueText = rootInstr.createTextNode(thiskey)
            idChild.appendChild(valueText)
            modeNode.appendChild(idChild)

            # <name>TxMasksAll</name>
            nameChild = rootInstr.createElement('name')
            valueText = rootInstr.createTextNode(nametoidl(str(thisnode['subject'])))
            nameChild.appendChild(valueText)
            modeNode.appendChild(nameChild)

            # <node-type-id type="integer">6</node-type-id>
            nodeTypeChild = rootInstr.createElement('node-type-id')
            nodeTypeChild.setAttribute("type", "integer")
            valueText = rootInstr.createTextNode("6")
            nodeTypeChild.appendChild(valueText)
            modeNode.appendChild(nodeTypeChild)

            # <project-id type="integer">13</project-id>
            projectIdChild = rootInstr.createElement('project-id')
            projectIdChild.setAttribute("type", "integer")
            valueText = rootInstr.createTextNode("13")
            projectIdChild.appendChild(valueText)
            modeNode.appendChild(projectIdChild)

            # <type>Mode</type>
            typeChild = rootInstr.createElement('type')
            valueText = rootInstr.createTextNode("Mode")
            typeChild.appendChild(valueText)
            modeNode.appendChild(typeChild)

            # <destinations type="array">
            # <destination type="Value">
            #    <id type="integer">504</id>
            # </destination>
            # <destination type="Value">
            #    <id type="integer">505</id>
            # </destination>
            # <destination type="Value">
            #    <id type="integer">503</id>
            # </destination>
            # </destinations>
            destsnode = rootInstr.createElement('destinations')
            destsnode.setAttribute("type", "array")

            '''
            # If there are no blocking items (other modes or values) then we should create a virtual value
            # to be sure the player is showing a value and not just showing an empty slot.
            blocking_present = False
            '''
            # print("Blocking",thiskey,":",thisnode['blocking'])
            for destid in thisnode['blocking']:
                if (len(destid)>0):
                    print(destid)
                    # If exporting partial projects, the key should fail
                    if destid in nodes_dict.keys():
                        thisdest = nodes_dict[destid]
                        dest = rootInstr.createElement('destination')
                        if thisdest['tracker'] == "prValue" or thisdest['tracker'] == "prValFloat" or thisdest['tracker'] == "prValText":
                            dest.setAttribute("type", "Value")
                            blocking_present = True                        
                        else:
                            if thisdest['tracker'] == "prMode":
                                dest.setAttribute("type", "Mode")
                                blocking_present = True                        
                            else:
                                dest.setAttribute("type", "Error1!!!")
                                print("ERROR1!!")
                        
                        destidnode = rootInstr.createElement('id')
                        destidnode.setAttribute("type","integer")
                        valueText = rootInstr.createTextNode(str(thisdest['id']))
                        destidnode.appendChild(valueText)
                        dest.appendChild(destidnode)
                        destidnode = rootInstr.createElement('ident')
                        valueText = rootInstr.createTextNode(destid)
                        destidnode.appendChild(valueText)
                        dest.appendChild(destidnode)
                        destsnode.appendChild(dest)

                    else:
                        print("The key",destid,"is not found, maybe you are exporting a partial project?")

            '''
            # If there are no blocking items (other modes or values) then we should create a virtual value
            # to be sure the player is showing a value and not just showing an empty slot.
            if not blocking_present:
                destid = str(-virtual_nodes_counter)
                destident = "VIRT"+str(-virtual_nodes_counter)
                virtual_nodes_counter += 1

                # A negative id
                valueNode = rootInstr.createElement('value')
                idChild = rootInstr.createElement('id')
                idChild.setAttribute("type", "integer")
                valueText = rootInstr.createTextNode(destid)
                idChild.appendChild(valueText)
                valueNode.appendChild(idChild)

                # A virtual identifier
                idChild = rootInstr.createElement('ident')
                valueText = rootInstr.createTextNode(destident)
                idChild.appendChild(valueText)
                valueNode.appendChild(idChild)

                # Same name than the mode
                nameChild = rootInstr.createElement('name')
                valueText = rootInstr.createTextNode(str(thisnode['subject']))
                nameChild.appendChild(valueText)
                valueNode.appendChild(nameChild)

                # <node-type-id type="integer">5</node-type-id>
                nodeTypeChild = rootInstr.createElement('node-type-id')
                nodeTypeChild.setAttribute("type", "integer")
                valueText = rootInstr.createTextNode("5")
                nodeTypeChild.appendChild(valueText)
                valueNode.appendChild(nodeTypeChild)

                # <project-id type="integer">13</project-id>
                projectIdChild = rootInstr.createElement('project-id')
                projectIdChild.setAttribute("type", "integer")
                valueText = rootInstr.createTextNode("13")
                projectIdChild.appendChild(valueText)
                valueNode.appendChild(projectIdChild)      

                # <type>Value</type>
                typeChild = rootInstr.createElement('type')
                valueText = rootInstr.createTextNode("Value")
                typeChild.appendChild(valueText)
                valueNode.appendChild(typeChild)            

                # <value-formatter-id type="integer" nil="true"></value-formatter-id>
                child = rootInstr.createElement('value-formatter-id')
                child.setAttribute("type", "integer")
                child.setAttribute("nil","true")
                valueNode.appendChild(child)

                # <destinations type="array"/>
                child = rootInstr.createElement('destinations')
                child.setAttribute("type", "array")
                valueNode.appendChild(child)
                
                # <node-attributes type="array"/>
                child = rootInstr.createElement('node-attributes')
                child.setAttribute("type", "array")
                valueNode.appendChild(child)

                # <labels type="array">
                child = rootInstr.createElement('labels')
                child.setAttribute("type", "array")
                valueNode.appendChild(child)

                xmlInstr.appendChild(valueNode)

                dest = rootInstr.createElement('destination')
                dest.setAttribute("type", "Value")
                destidnode = rootInstr.createElement('id')
                destidnode.setAttribute("type","integer")
                valueText = rootInstr.createTextNode(destid)
                destidnode.appendChild(valueText)
                dest.appendChild(destidnode)
                destidnode = rootInstr.createElement('ident')
                valueText = rootInstr.createTextNode(destident)
                destidnode.appendChild(valueText)
                dest.appendChild(destidnode)
                destsnode.appendChild(dest)
            '''
            
            modeNode.appendChild(destsnode)
            
            # <node-attributes type="array"/>
            child = rootInstr.createElement('node-attributes')
            child.setAttribute("type", "array")
            modeNode.appendChild(child)

            # <labels type="array">
            child = rootInstr.createElement('labels')
            child.setAttribute("type", "array")
            modeNode.appendChild(child)

            xmlInstr.appendChild(modeNode)

    # XML generation: second step is dump the subsystems
    # The order is important in this case, because one subsystem might only reference to 
    # previously defined ones


    for thiskey in sorted_nodes_dict:
        thisnode = nodes_dict[thiskey]
        '''
        <sub-system>
            <default-mode-id type="integer" nil="true"></default-mode-id>
            <id type="integer">499</id>
            <name>TxMasks</name>
            <node-type-id type="integer">4</node-type-id>
            <project-id type="integer">13</project-id>
            <type>SubSystem</type>
            <destinations type="array">
            <destination type="Value">
                <id type="integer">503</id>
            </destination>
            <destination type="Value">
                <id type="integer">504</id>
            </destination>
            <destination type="Value">
                <id type="integer">505</id>
            </destination>
            <destination type="Mode">
                <id type="integer">519</id>
            </destination>
            </destinations>
            <node-attributes type="array"/>
            <labels type="array">
            <label>
                <name>Masks</name>
                <scope-kind>
                <name>OPMS</name>
                </scope-kind>
            </label>
            </labels>
        </sub-system>'''
        if thisnode['tracker'] == "prSys" or thisnode['tracker'] == "prParam":
            sysNode = rootInstr.createElement('sub-system')

            # <default-mode-id type="integer" nil="true"></default-mode-id>
            idChild = rootInstr.createElement('default-mode-id')
            idChild.setAttribute("type", "integer")
            idChild.setAttribute("nil", "true")
            sysNode.appendChild(idChild)

            # <id type="integer">499</id>
            idChild = rootInstr.createElement('id')
            idChild.setAttribute("type", "integer")
            valueText = rootInstr.createTextNode(str(thisnode['id']))
            idChild.appendChild(valueText)
            sysNode.appendChild(idChild)

            idChild = rootInstr.createElement('ident')
            valueText = rootInstr.createTextNode(thiskey)
            idChild.appendChild(valueText)
            sysNode.appendChild(idChild)

            # <name>TxMasks</name>
            nameChild = rootInstr.createElement('name')
            valueText = rootInstr.createTextNode(nametoidl(str(thisnode['subject'])))
            nameChild.appendChild(valueText)
            sysNode.appendChild(nameChild)

            # <node-type-id type="integer">4</node-type-id>
            nodeTypeChild = rootInstr.createElement('node-type-id')
            nodeTypeChild.setAttribute("type", "integer")
            valueText = rootInstr.createTextNode("4")
            nodeTypeChild.appendChild(valueText)
            sysNode.appendChild(nodeTypeChild)

            # <project-id type="integer">13</project-id>
            projectIdChild = rootInstr.createElement('project-id')
            projectIdChild.setAttribute("type", "integer")
            valueText = rootInstr.createTextNode("13")
            projectIdChild.appendChild(valueText)
            sysNode.appendChild(projectIdChild)

            # <type>SubSystem</type>
            typeChild = rootInstr.createElement('type')
            valueText = rootInstr.createTextNode("SubSystem")
            typeChild.appendChild(valueText)
            sysNode.appendChild(typeChild)

            # <destinations type="array">
            #   <destination type="Value">
            #     <id type="integer">503</id>
            #   </destination>
            #   <destination type="Value">
            #     <id type="integer">504</id>
            #   </destination>
            #   <destination type="Value">
            #     <id type="integer">505</id>
            #   </destination>
            #   <destination type="Mode">
            #     <id type="integer">519</id>
            #   </destination>
            # </destinations>

            child = rootInstr.createElement('destinations')
            child.setAttribute("type", "array")

            # print("Children",thiskey,":",thisnode['children'])
            for destid in thisnode['children']:
                if (len(destid)>0):
                    # print(destid)
                    thisdest = nodes_dict[destid]
                    dest = rootInstr.createElement('destination')
                    if thisdest['tracker'] == "prValue" or thisdest['tracker'] == "prValFloat" or thisdest['tracker'] == "prValText":
                        dest.setAttribute("type", "Value")
                    else:
                        if thisdest['tracker'] == "prMode":
                            dest.setAttribute("type", "Mode")
                        
                        else:
                            if thisdest['tracker'] == "prSys" or thisdest['tracker'] == 'prParam':
                                dest.setAttribute("type", "SubSystem")

                            else:
                                if thisdest['tracker'] == "prCmd":
                                    valueText = thisdest['subject']
                                    dest.setAttribute("type", "Cmd")               

                                else:
                                    dest.setAttribute("type", "Error2!!!")
                                    print("Error2!! Check if the cosmoSys project PORIS trackers are enabled in the project settings.  Probably the tracker was changed from pr* to 'Bug' when importing")

                    destidnode = rootInstr.createElement('id')
                    destidnode.setAttribute("type","integer")
                    valueText = rootInstr.createTextNode(str(thisdest['id']))
                    destidnode.appendChild(valueText)
                    dest.appendChild(destidnode)
                    destidnode = rootInstr.createElement('ident')
                    valueText = rootInstr.createTextNode(destid)
                    destidnode.appendChild(valueText)
                    dest.appendChild(destidnode)
                    child.appendChild(dest)

            sysNode.appendChild(child)
            
            # <node-attributes type="array"/>
            child = rootInstr.createElement('node-attributes')
            child.setAttribute("type", "array")
            sysNode.appendChild(child)

            # <labels type="array">
            child = rootInstr.createElement('labels')
            child.setAttribute("type", "array")
            sysNode.appendChild(child)

            xmlInstr.appendChild(sysNode)




    xml_str = rootInstr.toprettyxml(indent ="    ",encoding="UTF-8") 

    filename = args.sys_file.name
    dirname = os.path.dirname(filename)
    basenamelist = os.path.splitext(os.path.basename(filename))
    onlyname = basenamelist[0]
    extension = basenamelist[1]
    xmlextension = ".xml"
    save_path_file = os.path.join(dirname,onlyname+xmlextension)

    with open(save_path_file, "wb") as f:
        f.write(xml_str) 

# Loads the ODS file into a nodes dictionary
nodes_dict = loadODS()

# Creates the instrument PORIS XML
createPorisXML(nodes_dict,deviceName)
