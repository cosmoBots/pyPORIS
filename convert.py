# Importing auxiliar libraries for the test
import argparse                     # This library allows us to easily parse the command line arguments

from pyexcel_ods import get_data    # This function allows us to easily read an ODS file (for api)
from xml.dom import minidom

# Importing test configuration file
import config

######### WE WILL PARSE THE COMMAND LINE ARGUMENTS FOR THE WRAPPER GEN #############
parser = argparse.ArgumentParser(description='Launches a PORIS xml generation from an ODS file describing the PORIS instrument')

## The second argument is the api ODS file
parser.add_argument('sys_file',type=argparse.FileType('r'), help="the path of a file containing the PORIS instrument description")

# Obtaining the arguments from the command line
args=parser.parse_args()

# Printing the obtained arguments:
print("The PORIS instrument description ODS filename is:",args.sys_file.name)

# As an example of a constant defined in the configuration file, we'll print the welcome message
print(config.welcome_message)

# Now we read the PORIS instrument description from the file file
nodesdata = get_data(args.sys_file.name,start_row=config.desc_file_start_row, row_limit=config.desc_file_row_limit, 
    start_column=config.desc_file_start_column,column_limit=config.desc_file_column_limit)[config.desc_file_sheet]

root = minidom.Document()
xml = root.createElement('sub-systems-v4')
root.appendChild(xml)

nodes_dict = {}
for row in nodesdata:
    if (len(row)>1):
        thiskey = row[config.desc_ident_column]
        if (len(thiskey)>0):
            # print(thiskey)

            thisnode = {}
            thisnode['ident'] = thiskey
            thisnode['id'] = row[config.desc_id_column]
            thisnode['subject'] = row[config.desc_subject_column]
            thisnode['description'] = row[config.desc_description_column]
            thisnode['parent'] = row[config.desc_parent_column]
            blockingstr = row[config.desc_blocking_column]
            thisnode['blocking'] = []
            if blockingstr is not None:
                thisnode['blocking'] = [x.strip() for x in blockingstr.split(',')]
            else:
                thisnode['blocking'] = []

            # print("Parsed:",thisnode['blocking'])
            thisnode['tracker'] = row[config.desc_tracker_column]
            thisnode['min'] = row[config.desc_min_column]
            thisnode['def'] = row[config.desc_def_column]
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
    '''
    if thisnode['tracker'] == "prValue" or thisnode['tracker'] == "prValFloat" or thisnode['tracker'] == "prValText":

        if thisnode['tracker'] == "prValue":
            valueNode = root.createElement('value')
        else:
            if thisnode['tracker'] == "prValFloat":
                valueNode = root.createElement('value-double-range')

            else:
                valueNode = root.createElement('Error!!!')

        # common part
        # <id type="integer">503</id>
        idChild = root.createElement('id')
        idChild.setAttribute("type", "integer")
        valueText = root.createTextNode(str(thisnode['id']))
        idChild.appendChild(valueText)
        valueNode.appendChild(idChild)

        idChild = root.createElement('ident')
        valueText = root.createTextNode(thiskey)
        idChild.appendChild(valueText)
        valueNode.appendChild(idChild)

        # <name>Tx2.0</name>
        nameChild = root.createElement('name')
        valueText = root.createTextNode(str(thisnode['subject']))
        nameChild.appendChild(valueText)
        valueNode.appendChild(nameChild)

        # <node-type-id type="integer">5</node-type-id>
        nodeTypeChild = root.createElement('node-type-id')
        nodeTypeChild.setAttribute("type", "integer")
        valueText = root.createTextNode("5")
        nodeTypeChild.appendChild(valueText)
        valueNode.appendChild(nodeTypeChild)        

        # <project-id type="integer">13</project-id>
        projectIdChild = root.createElement('project-id')
        projectIdChild.setAttribute("type", "integer")
        valueText = root.createTextNode("13")
        projectIdChild.appendChild(valueText)
        valueNode.appendChild(projectIdChild)

        if thisnode['tracker'] == "prValue":
            # <type>Value</type>
            typeChild = root.createElement('type')
            valueText = root.createTextNode("Value")
            typeChild.appendChild(valueText)
            valueNode.appendChild(typeChild)            

            # <value-formatter-id type="integer" nil="true"></value-formatter-id>
            child = root.createElement('value-formatter-id')
            child.setAttribute("type", "integer")
            child.setAttribute("nil","true")
            valueNode.appendChild(child)

        else:
            if thisnode['tracker'] == "prValFloat":
                # <type>ValueDoubleRange</type>
                typeChild = root.createElement('type')
                valueText = root.createTextNode("ValueDoubleRange")
                typeChild.appendChild(valueText)
                valueNode.appendChild(typeChild)

                # <value-formatter-id type="integer">5</value-formatter-id>
                child = root.createElement('value-formatter-id')
                child.setAttribute("type", "integer")
                valueText = root.createTextNode("5")
                child.appendChild(valueText)
                valueNode.appendChild(child)

                min_value = str(thisnode['min'])
                default_value = str(thisnode['def'])
                max_value = str(thisnode['max'])

                # <default-float type="float">0.01</default-float>
                child = root.createElement('default-float')
                child.setAttribute("type", "float")
                valueText = root.createTextNode(default_value)
                child.appendChild(valueText)
                valueNode.appendChild(child)

                # <rangemax type="float">1000.0</rangemax>
                child = root.createElement('rangemax')
                child.setAttribute("type", "float")
                valueText = root.createTextNode(max_value)
                child.appendChild(valueText)
                valueNode.appendChild(child)

                # <rangemin type="float">0.0</rangemin>
                child = root.createElement('rangemin')
                child.setAttribute("type", "float")
                valueText = root.createTextNode(min_value)
                child.appendChild(valueText)
                valueNode.appendChild(child)                

        # <destinations type="array"/>
        child = root.createElement('destinations')
        child.setAttribute("type", "array")
        valueNode.appendChild(child)
        
        # <node-attributes type="array"/>
        child = root.createElement('node-attributes')
        child.setAttribute("type", "array")
        valueNode.appendChild(child)

        # <labels type="array">
        child = root.createElement('labels')
        child.setAttribute("type", "array")
        valueNode.appendChild(child)

        xml.appendChild(valueNode)

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
                        print("child:",childkey,nodes_dict[childkey]['subject'],childlevel)
                        if childlevel == "prParam" or childlevel == "prSys":
                            if childkey not in sorted_nodes_dict:
                                includenode = False
                                print("oops!")
            else:
                if thisnode['tracker'] == "prMode":
                    print("trying to include:",nodekey,thisnode['subject'],thisnode['tracker'])
                    print(thisnode['blocking'])
                    for childkey in thisnode['blocking']:
                        if len(childkey)>0:
                            print("childkey:",childkey)
                            childlevel = nodes_dict[childkey]['tracker']
                            print("child:",childkey,nodes_dict[childkey]['subject'],childlevel)
                            if childkey not in sorted_nodes_dict:
                                includenode = False
                                print("oops!")
                

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
        modeNode = root.createElement('mode')

        # <default-mode-id type="integer" nil="true"></default-mode-id>
        idChild = root.createElement('default-mode-id')
        idChild.setAttribute("type", "integer")
        idChild.setAttribute("nil", "true")
        modeNode.appendChild(idChild)

        # <default-value-id type="integer" nil="true"></default-value-id>
        idChild = root.createElement('default-value-id')
        idChild.setAttribute("type", "integer")
        idChild.setAttribute("nil", "true")
        modeNode.appendChild(idChild)

        # <id type="integer">519</id>
        idChild = root.createElement('id')
        idChild.setAttribute("type", "integer")
        valueText = root.createTextNode(str(thisnode['id']))
        idChild.appendChild(valueText)
        modeNode.appendChild(idChild)

        idChild = root.createElement('ident')
        valueText = root.createTextNode(thiskey)
        idChild.appendChild(valueText)
        modeNode.appendChild(idChild)

        # <name>TxMasksAll</name>
        nameChild = root.createElement('name')
        valueText = root.createTextNode(str(thisnode['subject']))
        nameChild.appendChild(valueText)
        modeNode.appendChild(nameChild)

        # <node-type-id type="integer">6</node-type-id>
        nodeTypeChild = root.createElement('node-type-id')
        nodeTypeChild.setAttribute("type", "integer")
        valueText = root.createTextNode("6")
        nodeTypeChild.appendChild(valueText)
        modeNode.appendChild(nodeTypeChild)

        # <project-id type="integer">13</project-id>
        projectIdChild = root.createElement('project-id')
        projectIdChild.setAttribute("type", "integer")
        valueText = root.createTextNode("13")
        projectIdChild.appendChild(valueText)
        modeNode.appendChild(projectIdChild)

        # <type>Mode</type>
        typeChild = root.createElement('type')
        valueText = root.createTextNode("Mode")
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
        child = root.createElement('destinations')
        child.setAttribute("type", "array")

        # print("Blocking",thiskey,":",thisnode['blocking'])
        for destid in thisnode['blocking']:
            if (len(destid)>0):
                # print(destid)
                thisdest = nodes_dict[destid]
                dest = root.createElement('destination')
                if thisdest['tracker'] == "prValue" or thisdest['tracker'] == "prValFloat" or thisdest['tracker'] == "prValText":
                    dest.setAttribute("type", "Value")
                else:
                    if thisdest['tracker'] == "prMode":
                        dest.setAttribute("type", "Mode")
                    
                    else:
                        dest.setAttribute("type", "Error!!!")
                
                destidnode = root.createElement('id')
                destidnode.setAttribute("type","integer")
                valueText = root.createTextNode(str(thisdest['id']))
                destidnode.appendChild(valueText)
                dest.appendChild(destidnode)
                destidnode = root.createElement('ident')
                valueText = root.createTextNode(destid)
                destidnode.appendChild(valueText)
                dest.appendChild(destidnode)
                child.appendChild(dest)

        modeNode.appendChild(child)
        
        # <node-attributes type="array"/>
        child = root.createElement('node-attributes')
        child.setAttribute("type", "array")
        modeNode.appendChild(child)

        # <labels type="array">
        child = root.createElement('labels')
        child.setAttribute("type", "array")
        modeNode.appendChild(child)

        xml.appendChild(modeNode)

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
        sysNode = root.createElement('sub-system')

        # <default-mode-id type="integer" nil="true"></default-mode-id>
        idChild = root.createElement('default-mode-id')
        idChild.setAttribute("type", "integer")
        idChild.setAttribute("nil", "true")
        sysNode.appendChild(idChild)

        # <id type="integer">499</id>
        idChild = root.createElement('id')
        idChild.setAttribute("type", "integer")
        valueText = root.createTextNode(str(thisnode['id']))
        idChild.appendChild(valueText)
        sysNode.appendChild(idChild)

        idChild = root.createElement('ident')
        valueText = root.createTextNode(thiskey)
        idChild.appendChild(valueText)
        sysNode.appendChild(idChild)

        # <name>TxMasks</name>
        nameChild = root.createElement('name')
        valueText = root.createTextNode(str(thisnode['subject']))
        nameChild.appendChild(valueText)
        sysNode.appendChild(nameChild)

        # <node-type-id type="integer">4</node-type-id>
        nodeTypeChild = root.createElement('node-type-id')
        nodeTypeChild.setAttribute("type", "integer")
        valueText = root.createTextNode("4")
        nodeTypeChild.appendChild(valueText)
        sysNode.appendChild(nodeTypeChild)

        # <project-id type="integer">13</project-id>
        projectIdChild = root.createElement('project-id')
        projectIdChild.setAttribute("type", "integer")
        valueText = root.createTextNode("13")
        projectIdChild.appendChild(valueText)
        sysNode.appendChild(projectIdChild)

        # <type>SubSystem</type>
        typeChild = root.createElement('type')
        valueText = root.createTextNode("SubSystem")
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

        child = root.createElement('destinations')
        child.setAttribute("type", "array")

        # print("Children",thiskey,":",thisnode['children'])
        for destid in thisnode['children']:
            if (len(destid)>0):
                # print(destid)
                thisdest = nodes_dict[destid]
                dest = root.createElement('destination')
                if thisdest['tracker'] == "prValue" or thisdest['tracker'] == "prValFloat" or thisdest['tracker'] == "prValText":
                    dest.setAttribute("type", "Value")
                else:
                    if thisdest['tracker'] == "prMode":
                        dest.setAttribute("type", "Mode")
                    
                    else:
                        if thisdest['tracker'] == "prSys" or thisdest['tracker'] == 'prParam':
                            dest.setAttribute("type", "SubSystem")
                        
                        else:
                            dest.setAttribute("type", "Error!!!")

                destidnode = root.createElement('id')
                destidnode.setAttribute("type","integer")
                valueText = root.createTextNode(str(thisdest['id']))
                destidnode.appendChild(valueText)
                dest.appendChild(destidnode)
                destidnode = root.createElement('ident')
                valueText = root.createTextNode(destid)
                destidnode.appendChild(valueText)
                dest.appendChild(destidnode)
                child.appendChild(dest)

        sysNode.appendChild(child)
        
        # <node-attributes type="array"/>
        child = root.createElement('node-attributes')
        child.setAttribute("type", "array")
        sysNode.appendChild(child)

        # <labels type="array">
        child = root.createElement('labels')
        child.setAttribute("type", "array")
        sysNode.appendChild(child)

        xml.appendChild(sysNode)




xml_str = root.toprettyxml(indent ="\t",encoding="UTF-8") 
save_path_file = "instrument.xml"

with open(save_path_file, "wb") as f:
    f.write(xml_str) 

