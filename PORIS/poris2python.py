# Importing auxiliar libraries for the test
import argparse                     # This library allows us to easily parse the command line arguments

from pyexcel_ods import get_data    # This function allows us to easily read an ODS file (for api)
from xml.dom import minidom
from pathlib import Path
import os

# Importing test configuration file
import config

generate_oldcode = False

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
                            if nodes_dict[ch]['tracker'] == "prMode":
                                if nodes_dict[ch]['virtual'] == False:
                                    virtnode['blocking'] += [ch]
                                    print(ch,nodes_dict[ch]['subject'],"bloquea a",virtident,virtnode['description'])
                                    #print(virtnode['blocking'])

                if len(virtnode['blocking']) > 0:
                    nodes_to_add[virtident] = virtnode
                    thisnode['children'].append(virtident)

    tree_dict = {}
    print("hola",len(tree_dict),len(nodes_dict))
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



# This function will create, in parallel:
# - The $S1.py
# - The $S1PORIS.py

methods_dict = {}

def createCxxCode(nodes_dict,deviceName):
    global methods_dict
    # Now we read the methods list from the file
    functionsfile = "./"+deviceName+".user/methods.ods"
    functionsdata = get_data(functionsfile,start_row=config.methods_file_start_row, row_limit=config.methods_file_row_limit, 
        start_column=config.methods_file_start_column,column_limit=config.methods_file_column_limit)[config.methods_file_sheet]



    for row in functionsdata:
        if (len(row)>1):
            thiskey = row[config.methods_function_column]
            if (len(thiskey)>0):
                print(thiskey)
                thisnode = {}
                thisnode['method'] = thiskey
                thisnode['node'] = row[config.methods_node_column]
                methods_dict[thiskey] = thisnode

    methodsstr =  "\t//----------------------------------------------------------------------\n"
    methodsstr += "\t//  Specific methods\n"
    methodsstr += "\t//----------------------------------------------------------------------\n\n"
    methodsstr += "\tpublic:\n\n"

    for key in methods_dict.keys():
        m = methods_dict[key]
        methodsstr += '\t/** boolean '+key+' */\n\boolean '+key+'(boolean value);\n\n'

    magsstr = "\tprivate:\n\n"

    magsstr += "//Including fragment for PORIS support\n"
    magsstr +=  "#include \"_"+deviceName+"PORIS.h\"\n\n"

    magsstr +=  "\t//----------------------------------------------------------------------\n"
    magsstr += "\t//  Device Magnitudes\n"
    magsstr += "\t//----------------------------------------------------------------------\n\n"

    porishstr =  "#ifndef _"+deviceName+"PORIS_H\n"
    porishstr += "#define _"+deviceName+"PORIS_H\n\n"
    poriscstr =  "#include \""+deviceName+".h\"\n\n"

    poriscsyncstr = "bool "+deviceName+"::sync_PORIS_Model(void){\n"
    poriscinitstr = "PORISSys *"+deviceName+"::PORIS_init(void){\n\tint identcounter = 0;\n\n"
    poriscinitretstr = ""
    poriscinitrelstr = ""

    closefuncstr = "\n\treturn ret;\n}\n\n"

    for thiskey in nodes_dict.keys():    
        thisnode = nodes_dict[thiskey]
        nodename = nametoidl(thisnode['subject'])
        thisclass = thisnode['tracker']

        if thisclass == "prParam" or thisclass == "prSys":

            enumname = "enum_"+nodename
            enummodename = enumname+"Mode"
            choicesname = nodename+"ChoiceList"

            nodevar = "enum"+nodename
            modevar = "enum"+nodename+"Mode"

            modevar_ = modevar+"_"
            nodevar_ = nodevar+"_"     
            '''
                /** Process enum */
                enum_EnumMon processEnum(enum_EnumMon value);
            '''
            if thisclass == "prParam":
                # PORISParam prBinning;
                porishstr += "PORISParam pr"+nodename+";\n"
                porishstr += "PORISMode pr"+nodename+"Mode_UNKNOWN;\n"
                porishstr += "PORISValue pr"+nodename+"_UNKNOWN;\n"

                poriscsyncstr += "\t// Param "+nodename+"\n"

                methodsstr += "\t// --------- "+thisclass+" "+nodename+" -----------------\n"
                methodsstr += "\t/* "+nodename+" */\n"
                methodsstr += "\t"+enumname+" get_"+nodename+"(void);\n"
                methodsstr += "\t"+enumname+" set_"+nodename+"("+enumname+" value);\n"
                '''
                prBinning.id = identcounter++;
                prBinning.idx = 1;
                prBinning.ident = "Binning";
                prBinning.name = "Binning";
                prBinning.description = "Parametro de binning";
                prBinning.parent = &prDetector;
                prDetector.params.push_back(&prBinning);

                prBinning_UNKNOWN.id = identcounter++;
                prBinning_UNKNOWN.idx = MyDASDevice::Binning_UNKNOWN;
                prBinning_UNKNOWN.ident = "Binning_UNKNOWN";
                prBinning_UNKNOWN.name = "Binning_UNKNOWN";
                prBinning_UNKNOWN.description = "Binning_UNKNOWN";
                prBinning_UNKNOWN.parent = &prBinning;
                prBinning.values.push_back(&prBinning_UNKNOWN);

                prBinningMode_UNKNOWN.id = identcounter++;
                prBinningMode_UNKNOWN.idx = MyDASDevice::BinningMode_UNKNOWN;    
                prBinningMode_UNKNOWN.ident = "BinningMode_UNKNOWN";
                prBinningMode_UNKNOWN.name = "BinningMode_UNKNOWN";
                prBinningMode_UNKNOWN.description = "BinningMode_UNKNOWN";
                prBinningMode_UNKNOWN.parent = &prBinning;
                prBinning.modes.push_back(&prBinningMode_UNKNOWN);
                prBinningMode_UNKNOWN.values.push_back(&prBinning_UNKNOWN);

                prDetectorMode_UNKNOWN.submodes.push_back(&prBinningMode_UNKNOWN);

                '''
                parentNode = None
                parentNodeName = ""
                if 'parentnode' in thisnode.keys():
                    parentNode = thisnode['parentnode']
                    parentNodeName = nametoidl(parentNode['subject'])
                    if 'paramcounter' in parentNode.keys():
                        counter = parentNode['paramcounter']
                    else:
                        counter = 0
                    
                    parentNode['paramcounter'] = counter + 1
                else:
                    counter = 0

                poriscinitstr += "\n\tpr"+nodename+".id = identcounter++;\n"
                poriscinitstr += "\tpr"+nodename+".idx = "+str(counter)+";\n"
                poriscinitstr += "\tpr"+nodename+".ident = \""+nodename+"\";\n"
                poriscinitstr += "\tpr"+nodename+".name = \""+nodename+"\";\n"
                poriscinitstr += "\tpr"+nodename+".description = \""+desctomonit(thisnode['description'])+"\";\n"
                if parentNode is not None:
                    poriscinitstr += "\tpr"+nodename+".parent = &pr"+parentNodeName+";\n"
                    poriscinitstr += "\tpr"+parentNodeName+".params.push_back(&pr"+nodename+");\n" 
                else:
                    poriscinitstr += "\tpr"+nodename+".parent = NULL;\n"

                poriscinitstr += "\n\tpr"+nodename+ "_UNKNOWN.id = identcounter++;\n"
                poriscinitstr += "\tpr"+nodename+ "_UNKNOWN.idx = "+deviceName+"::"+nodename+ "_UNKNOWN;\n"
                poriscinitstr += "\tpr"+nodename+ "_UNKNOWN.ident = \""+nodename+ "_UNKNOWN\";\n"
                poriscinitstr += "\tpr"+nodename+ "_UNKNOWN.name = \""+nodename+ "_UNKNOWN\";\n"
                poriscinitstr += "\tpr"+nodename+ "_UNKNOWN.description = \"Unknown value for "+nodename+"\";\n"
                poriscinitstr += "\tpr"+nodename+ "_UNKNOWN.parent = &pr"+nodename+";\n"
                poriscinitstr += "\tpr"+nodename+".values.push_back(&pr"+nodename+ "_UNKNOWN);\n"

                poriscinitstr += "\n\tpr"+nodename+ "Mode_UNKNOWN.id = identcounter++;\n"
                poriscinitstr += "\tpr"+nodename+ "Mode_UNKNOWN.idx = "+deviceName+"::"+nodename+ "Mode_UNKNOWN;\n"
                poriscinitstr += "\tpr"+nodename+ "Mode_UNKNOWN.ident = \""+nodename+ "Mode_UNKNOWN\";\n"
                poriscinitstr += "\tpr"+nodename+ "Mode_UNKNOWN.name = \""+nodename+ "Mode_UNKNOWN\";\n"
                poriscinitstr += "\tpr"+nodename+ "Mode_UNKNOWN.description = \"Unknown mode for "+nodename+"\";\n"
                poriscinitstr += "\tpr"+nodename+ "Mode_UNKNOWN.parent = &pr"+nodename+";\n"
                poriscinitstr += "\tpr"+nodename+".modes.push_back(&pr"+nodename+ "Mode_UNKNOWN);\n"
                poriscinitstr += "\tpr"+nodename+ "Mode_UNKNOWN.values.push_back(&pr"+nodename+ "_UNKNOWN);\n"
                poriscinitstr += "\tpr"+parentNodeName+ "Mode_UNKNOWN.submodes.push_back(&pr"+nodename+ "Mode_UNKNOWN);\n"

            else:
                # PORISSys prDetector;
                porishstr += "PORISSys pr"+nodename+";\n"
                porishstr += "PORISMode pr"+nodename+"Mode_UNKNOWN;\n"

                poriscsyncstr += "\t// Sys "+nodename+"\n"

                parentNode = None
                parentNodeName = ""
                if 'parentnode' in thisnode.keys():
                    parentNode = thisnode['parentnode']
                    parentNodeName = nametoidl(parentNode['subject'])
                    if 'syscounter' in parentNode.keys():
                        counter = parentNode['syscounter']
                    else:
                        counter = 0
                    
                    parentNode['syscounter'] = counter + 1
                else:
                    counter = 0

                '''
                prDetector.id = identcounter++;
                prDetector.idx = 0;
                prDetector.ident = "Detector";
                prDetector.name = "Detector";
                prDetector.description = "Detector";
                prDetector.parent = NULL;
                '''
                poriscinitstr += "\n\tpr"+nodename+".id = identcounter++;\n"
                poriscinitstr += "\tpr"+nodename+".idx = "+str(counter)+";\n"
                poriscinitstr += "\tpr"+nodename+".ident = \""+nodename+"\";\n"
                poriscinitstr += "\tpr"+nodename+".name = \""+nodename+"\";\n"
                poriscinitstr += "\tpr"+nodename+".description = \""+desctomonit(thisnode['description'])+"\";\n"
                if parentNode is not None:
                    poriscinitstr += "\tpr"+nodename+".parent = &pr"+parentNodeName+";\n"
                    poriscinitstr += "\tpr"+parentNodeName+".subsystems.push_back(&pr"+nodename+");\n" 
                else:
                    poriscinitstr += "\tpr"+nodename+".parent = NULL;\n"
                    poriscinitretstr = "\n\treturn &pr"+nodename+";\n"                

                poriscinitstr += "\n\tpr"+nodename+ "Mode_UNKNOWN.id = identcounter++;\n"
                poriscinitstr += "\tpr"+nodename+ "Mode_UNKNOWN.idx = "+deviceName+"::"+nodename+ "Mode_UNKNOWN;\n"
                poriscinitstr += "\tpr"+nodename+ "Mode_UNKNOWN.ident = \""+nodename+ "Mode_UNKNOWN\";\n"
                poriscinitstr += "\tpr"+nodename+ "Mode_UNKNOWN.name = \""+nodename+ "Mode_UNKNOWN\";\n"
                poriscinitstr += "\tpr"+nodename+ "Mode_UNKNOWN.description = \""+desctomonit(thisnode['description'])+"\";\n"
                poriscinitstr += "\tpr"+nodename+ "Mode_UNKNOWN.parent = &pr"+nodename+";\n"
                poriscinitstr += "\tpr"+nodename+".modes.push_back(&pr"+nodename+ "Mode_UNKNOWN);\n"

            methodsstr += "\t/* "+nodename+"Mode */\n"
            methodsstr += "\t"+enummodename+" get_"+nodename+"Mode(void);\n"
            methodsstr += "\t"+enummodename+" set_"+nodename+"Mode("+enummodename+" value);\n\n"

            # methodsstr += "\t/* Get values for "+nodename+" in current */\n"
            # methodsstr += "\t"+choicesname+" getChoicesFor"+nodename+"();\n\n"

            if thisclass == "prParam":
                if generate_oldcode:
                    funcstr = "bool check"+nodename+"Elibility("+nodename+" value)"
                    porishstr += funcstr+";\n"
                    poriscstrfp1 = "bool "+deviceName+"::check"+nodename+"Elibility("+nodename+" value)"+"{\n"
                    poriscstrfp1 += "\tbool ret = false;\n\n"

                    funcstr = nodename+" getEligible"+nodename+"(void)"
                    porishstr += funcstr+";\n"
                    poriscstrfp2 = deviceName+"::"+nodename+" "+deviceName+"::getEligible"+nodename+"(void)"+"{\n"
                    poriscstrfp2 += "\t"+nodename+" ret = "+nodename+"_UNKNOWN;\n\n"
                    poriscstrfp2 += "\tif (check"+nodename+"Elibility("+nodevar_+")){\n"
                    poriscstrfp2 += "\t\tret = "+nodevar_+";\n"
                    poriscstrfp2 += "\t} else {\n"
            if generate_oldcode:
                funcstr = "bool check"+nodename+"ModeElibility("+nodename+"Mode value)"
                porishstr += funcstr+";\n"
                poriscstrfm1 = "bool "+deviceName+"::check"+nodename+"ModeElibility("+nodename+"Mode value)"+"{\n"
                if 'parentnode' in thisnode.keys():
                    poriscstrfm1 += "\tbool ret = false;\n\n"

                else:
                    poriscstrfm1 += "\tbool ret = true;\n\n"

            if generate_oldcode:
                funcstr = nodename+"Mode getEligible"+nodename+"Mode(void)"
                porishstr += funcstr+";\n\n"
                poriscstrfm2 = deviceName+"::"+nodename+"Mode "+deviceName+"::getEligible"+nodename+"Mode(void)"+"{\n"
                poriscstrfm2 += "\t"+nodename+"Mode ret = "+nodename+"Mode_UNKNOWN;\n\n"        
                poriscstrfm2 += "\tif (check"+nodename+"ModeElibility("+modevar_+")){\n"
                poriscstrfm2 += "\t\tret = "+modevar_+";\n"
                poriscstrfm2 += "\t} else {\n"

            magsstr += "\t// --------- "+thisclass+" "+nodename+" -----------------\n"
            if thisclass == "prParam":
                magsstr += "\t/**\n"
                magsstr += "\t* Enum "+nodename+"\n"
                magsstr += "\t* @description Enum "+desctomonit(thisnode['description'])+"\n"
    
            modestr = "\t/**\n"
            modestr += "\t* Enum "+nodename+"Mode\n"
            modestr += "\t* @description Enum [Mode]"+desctomonit(thisnode['description'])+"\n"

            if thisclass == "prParam":
                valuesstr = nodename+"_UNKNOWN"
                valuesshortstr = "UNKNOWN"
                valuemaxstr = valuesstr
            
            modeliststr = nodename+"Mode_UNKNOWN"
            modeshortliststr = "UNKNOWN"
            modemaxstr = modeliststr
            switchfm2 = False
            if 'parentnode' in thisnode.keys():
                parentnode = thisnode['parentnode']
                if parentnode is not None:
                    parentnodename = nametoidl(parentnode['subject'])
                    parentnodeclass = parentnode['tracker']
                    parentnodevar = "enum"+parentnodename
                    parentmodevar = "enum"+parentnodename+"Mode"
                    parentmodevar_ = parentmodevar+"_"
                    parentnodevar_ = parentnodevar+"_"
                    parentnodemodevar = parentnode
                    if generate_oldcode:
                        poriscstrfm1sw = "\tswitch ("+parentmodevar_+"){\n"
                        poriscstrfm2 += "\t\tswitch ("+parentmodevar_+"){\n"
                        switchfm2 = True
                        anyvaluepresentparentouter = False

                    for k in parentnode['children']:
                        childnode = nodes_dict[k]
                        childname = nametoidl(childnode['subject'])
                        childclass = childnode['tracker']
                        if childclass == "prMode":
                            anyvaluepresentparentinner = False
                            firstfound = False                        
                            if generate_oldcode:
                                poriscstrfm1sw2 = "\t\tcase "+parentnodename+"Mode_"+childname+":\n"
                                poriscstrfm1sw2 += "\t\t\tswitch (value){\n"
                            
                            for kv in childnode['blocking']:
                                kvnode = nodes_dict[kv]
                                kvname = nametoidl(kvnode['subject'])
                                kvclass = kvnode['tracker']
                                if kvclass == "prMode":
                                    if kvnode['parentnode'] == thisnode:
                                        if generate_oldcode:
                                            poriscstrfm1sw2 += "\t\t\t\tcase "+nodename+"Mode_"+kvname+":\n"
                                        
                                        poriscinitrelstr += "\t// Marcamos "+nodename+"Mode_"+kvname+" como elegible para "+parentnodename+"Mode_"+childname+"\n"
                                        poriscinitrelstr += "\tpr"+parentnodename+"Mode_"+childname+".submodes.push_back(&pr"+nodename+"Mode_"+kvname+");\n"
                                        anyvaluepresentparentinner = True
                                        if not firstfound:
                                            firstfound = True
                                            if generate_oldcode:
                                                poriscstrfm2 += "\t\t\tcase "+parentnodename+"Mode_"+childname+":\n"
                                                poriscstrfm2 += "\t\t\t\tret = "+nodename+"Mode_"+kvname+";\n"
                                                poriscstrfm2 += "\t\t\t\tbreak;\n"

                            if (anyvaluepresentparentinner):
                                anyvaluepresentparentouter = True
                                if generate_oldcode:                            
                                    poriscstrfm1sw2 += "\t\t\t\t\tret = true;\n"
                                    poriscstrfm1sw2 += "\t\t\t\t\tbreak;\n"
                                    poriscstrfm1sw2 += "\t\t\t}\n"
                                    poriscstrfm1sw2 += "\t\t\tbreak;\n"
                                    poriscstrfm1sw += poriscstrfm1sw2

                    if anyvaluepresentparentouter:
                        if generate_oldcode:                        
                            poriscstrfm1sw += "\t}\n"
                            poriscstrfm1 += poriscstrfm1sw


            else:
                parentnode = None

            if generate_oldcode:
                switchfp2 = False

            monitsetparam = None
            magsstrfl = ""
            methodsstrfl = ""
            minimum_float = None
            maximum_float = None
            if thisclass == "prParam":
                if generate_oldcode:
                    poriscstrfp1sw = "\tswitch ("+modevar_+"){\n"
                    poriscstrfp2 += "\t\tswitch ("+modevar_+"){\n"
                    switchfp2 = True
                for k in thisnode['children']:
                    childnode = nodes_dict[k]
                    childname = nametoidl(childnode['subject'])
                    childclass = childnode['tracker']
                    if childclass == "prMode":
                        modeliststr += ","+nodename+"Mode_"+childname
                        modeshortliststr += ","+childname
                        modemaxstr = nodename+"Mode_"+childname

                        anyvaluepresentinner = False
                        firstdone = False                    
                        if generate_oldcode:
                            poriscstrfp1sw2 = "\t\tcase "+nodename+"Mode_"+childname+":\n"
                            poriscstrfp1sw2 += "\t\t\tswitch (value){\n"
                        

                        for kv in childnode['blocking']:
                            kvnode = nodes_dict[kv]
                            kvname = nametoidl(kvnode['subject'])
                            kvclass = kvnode['tracker']
                            if kvclass == "prValFloat" or kvclass == "prValText" or kvclass == "prValue":
                                if generate_oldcode:
                                    poriscstrfp1sw2 += "\t\t\t\tcase "+nodename+"_"+kvname+":\n"
                                
                                if kvnode['virtual'] == False:
                                    poriscinitrelstr += "\t// Marcamos "+nodename+"_"+kvname+" como elegible para "+nodename+"Mode_"+childname+"\n"
                                    poriscinitrelstr += "\tpr"+nodename+"Mode_"+childname+".values.push_back(&pr"+nodename+"_"+kvname+");\n"

                                anyvaluepresentinner = True
                                if not firstdone:
                                    firstdone = True
                                    if generate_oldcode:
                                        poriscstrfp2 += "\t\t\tcase "+nodename+"Mode_"+childname+":\n"
                                        poriscstrfp2 += "\t\t\t\tret = "+nodename+"_"+kvname+";\n"
                                        poriscstrfp2 += "\t\t\t\tbreak;\n"

                                if kvclass == "prValFloat":
                                    magsstrfl = "\t// "+thisclass+" "+nodename+"Double -----------------\n"
                                    magsstrfl += "\t/**\n"
                                    magsstrfl += "\t* double "+nodename+"Double\n"
                                    magsstrfl += "\t* @description double "+desctomonit(thisnode['description'])+"\n"
                                    if maximum_float is None:
                                        maximum_float = kvnode['max']
                                    else:
                                        maximum_float = max(maximum_float,kvnode['max'])

                                    if minimum_float is None:
                                        minimum_float = kvnode['min']
                                    else:
                                        minimum_float = min(minimum_float,kvnode['min'])

                                    magsstrfl += "\t* @maximum     $$MAX\n"
                                    magsstrfl += "\t* @minimum     $$MIN\n"
                                    magsstrfl += "\t*/\n"
                                    magsstrfl += "\tdouble "+nodename+"Double;\n\n"
                                    methodsstrfl = "\t// --------- "+thisclass+" "+parentNodeName+" -----------------\n"
                                    methodsstrfl += "\t/* "+nodename+"Double */\n"
                                    methodsstrfl += "\tdouble get_"+nodename+"Double(void);\n"
                                    methodsstrfl += "\tdouble set_"+nodename+"Double(double value);\n\n"

                                if kvclass == "prValText":
                                    magsstrfl = "\t// "+thisclass+" "+nodename+"String -----------------\n"
                                    magsstrfl += "\t/**\n"
                                    magsstrfl += "\t* string "+nodename+"String\n"
                                    magsstrfl += "\t* @description string "+desctomonit(thisnode['description'])+"\n"
                                    magsstrfl += "\t* @default     "+kvnode['deftext']+"\n"
                                    magsstrfl += "\t*/\n"
                                    magsstrfl += "\tstring "+nodename+"String;\n\n"
                                    methodsstrfl = "\t// --------- "+thisclass+" "+parentNodeName+" -----------------\n"
                                    methodsstrfl += "\t/* "+nodename+"String */\n"
                                    methodsstrfl += "\tstring get_"+nodename+"String(void);\n" 
                                    methodsstrfl += "\tstring set_"+nodename+"String(string value);\n\n" 
             

                        if (anyvaluepresentinner):
                                anyvaluepresentouter = True
                                if generate_oldcode:
                                    poriscstrfp1sw2 += "\t\t\t\t\tret = true;\n"
                                    poriscstrfp1sw2 += "\t\t\t\t\tbreak;\n"
                                    poriscstrfp1sw2 += "\t\t\t}\n"
                                    poriscstrfp1sw2 += "\t\t\tbreak;\n"
                                    poriscstrfp1sw += poriscstrfp1sw2                        
                    else:
                        if childclass == "prValFloat" or childclass == "prValText" or childclass == "prValue":
                            valuesstr += ","+nodename+"_"+childname
                            valuesshortstr += ","+childname
                            valuemaxstr = nodename+"_"+childname


                if anyvaluepresentouter:
                    if generate_oldcode:
                        poriscstrfp1sw += "\t}\n"
                        poriscstrfp1 += poriscstrfp1sw

                magsstr += "\t* @maximum     "+valuemaxstr+"\n"
                magsstr += "\t* @minimum     "+nodename+"_UNKNOWN"+"\n"
                magsstr += "\t* @values      "+valuesstr+"\n"
                magsstr += "\t*/\n"
                magsstr += "\tenum class "+enumname+" {"+ valuesstr+"};\n"
                magsstr += "\t"+enumname+" "+nodevar+";\n\n"


                methodsstr += methodsstrfl
                if (maximum_float is not None):
                    magsstrfl = magsstrfl.replace("$$MAX",str(maximum_float)).replace("$$MIN",str(minimum_float))
                    magsstr += magsstrfl
                    print(maximum_float,"|",minimum_float,"|",magsstrfl)

                else:
                    magsstr += magsstrfl

                if generate_oldcode:
                    if switchfp2:
                        poriscstrfp2 += "\t\t}\n"

                    poriscstrfp2 += "\t}\n"

                    poriscstrfp1 += closefuncstr
                    poriscstrfp2 += closefuncstr
                    poriscstr += poriscstrfp1 + poriscstrfp2

            else:
                if thisclass == "prSys":
                    for k in thisnode['children']:
                        childnode = nodes_dict[k]
                        childname = nametoidl(childnode['subject'])
                        childclass = childnode['tracker']
                        if childclass == "prMode":
                            modeliststr += ","+nodename+"Mode_"+childname
                            modeshortliststr += ","+childname
                            modemaxstr = nodename+"Mode_"+childname

            modestr += "\t* @maximum     "+modemaxstr+"\n"
            modestr += "\t* @minimum     "+nodename+"Mode_UNKNOWN\n"
            modestr += "\t* @values      "+modeliststr+"\n"
            modestr += "\t*/\n"
            modestr += "\tenum class "+enummodename+" {"+ modeliststr+"};\n"
            modestr += "\t"+enummodename+" "+modevar+";\n\n"
            magsstr += modestr

            if generate_oldcode:
                if switchfm2:
                    poriscstrfm2 += "\t\t}\n"

                poriscstrfm2 += "\t}\n"

                poriscstrfm1 += closefuncstr
                poriscstrfm2 += closefuncstr

                poriscstr += poriscstrfm1 + poriscstrfm2

        else:
            parentNode = thisnode['parentnode']
            parentNodeName = nametoidl(parentNode['subject'])
            if thisclass == "prMode":
                #PORISMode prDetectorMode_Image;
                porishstr += "PORISMode pr"+parentNodeName+ "Mode_" + nodename+";\n"
                '''
                prDetectorMode_UNKNOWN.id = identcounter++;
                prDetectorMode_UNKNOWN.idx = MyDASDevice::DetectorMode_UNKNOWN;
                prDetectorMode_UNKNOWN.ident = "DetectorMode_UNKNOWN";
                prDetectorMode_UNKNOWN.name = "DetectorMode_UNKNOWN";
                prDetectorMode_UNKNOWN.description = "DetectorMode_UNKNOWN";
                prDetectorMode_UNKNOWN.parent = &prDetector;
                '''
                poriscinitstr += "\n\tpr"+parentNodeName+ "Mode_" + nodename+".id = identcounter++;\n"
                poriscinitstr += "\tpr"+parentNodeName+ "Mode_" + nodename+".idx = "+deviceName+"::"+parentNodeName+ "Mode_" + nodename+";\n"
                poriscinitstr += "\tpr"+parentNodeName+ "Mode_" + nodename+".ident = \""+parentNodeName+ "Mode_" + nodename+"\";\n"
                poriscinitstr += "\tpr"+parentNodeName+ "Mode_" + nodename+".name = \""+parentNodeName+ "Mode_" + nodename+"\";\n"
                poriscinitstr += "\tpr"+parentNodeName+ "Mode_" + nodename+".description = \""+desctomonit(thisnode['description'])+"\";\n"
                poriscinitstr += "\tpr"+parentNodeName+ "Mode_" + nodename+".parent = &pr"+parentNodeName+";\n"
                poriscinitstr += "\tpr"+parentNodeName+".modes.push_back(&pr"+parentNodeName+ "Mode_" + nodename+");\n" 

            else:
                if thisclass == "prValue":
                    if thisnode['virtual'] == False:
                        #PORISValue prBinning_1x1;
                        porishstr += "PORISValue pr"+parentNodeName+ "_" + nodename+";\n"
                        '''
                        prBinning_1x1.id = identcounter++;
                        prBinning_1x1.idx = MyDASDevice::Binning_1x1;
                        prBinning_1x1.ident = "Binning_1x1";
                        prBinning_1x1.name = "Binning_1x1";
                        prBinning_1x1.description = "Sin binning";
                        prBinning_1x1.parent = &prBinning;
                        '''                
                        poriscinitstr += "\n\tpr"+parentNodeName+ "_" + nodename+".id = identcounter++;\n"
                        poriscinitstr += "\tpr"+parentNodeName+ "_" + nodename+".idx = "+deviceName+"::"+parentNodeName+ "_" + nodename+";\n"
                        poriscinitstr += "\tpr"+parentNodeName+ "_" + nodename+".ident = \""+parentNodeName+ "_" + nodename+"\";\n"
                        poriscinitstr += "\tpr"+parentNodeName+ "_" + nodename+".name = \""+parentNodeName+ "_" + nodename+"\";\n"
                        poriscinitstr += "\tpr"+parentNodeName+ "_" + nodename+".description = \""+desctomonit(thisnode['description'])+"\";\n"
                        poriscinitstr += "\tpr"+parentNodeName+ "_" + nodename+".parent = &pr"+parentNodeName+";\n"
                        poriscinitstr += "\tpr"+parentNodeName+".values.push_back(&pr"+parentNodeName+ "_" + nodename+");\n"

                else:
                    if thisclass == "prValFloat":             
                        #PORISValueFloat prExpTime_Normal;
                        porishstr += "PORISValueFloat pr"+parentNodeName+ "_" + nodename+";\n"
                        '''
                        prExpTime_Normal.id = identcounter++;
                        prExpTime_Normal.idx = MyDASDevice::ExpTime_Normal;
                        prExpTime_Normal.ident = "ExpTime_Normal";
                        prExpTime_Normal.name = "ExpTime_Normal";
                        prExpTime_Normal.description = "Rango normal de valores para ExpTime";
                        prExpTime_Normal.parent = &prExpTime;                    
                        '''                
                        poriscinitstr += "\n\tpr"+parentNodeName+ "_" + nodename+".id = identcounter++;\n"
                        poriscinitstr += "\tpr"+parentNodeName+ "_" + nodename+".idx = "+deviceName+"::"+parentNodeName+ "_" + nodename+";\n"
                        poriscinitstr += "\tpr"+parentNodeName+ "_" + nodename+".ident = \""+parentNodeName+ "_" + nodename+"\";\n"
                        poriscinitstr += "\tpr"+parentNodeName+ "_" + nodename+".name = \""+parentNodeName+ "_" + nodename+"\";\n"
                        poriscinitstr += "\tpr"+parentNodeName+ "_" + nodename+".description = \""+desctomonit(thisnode['description'])+"\";\n"
                        poriscinitstr += "\tpr"+parentNodeName+ "_" + nodename+".min = "+str(thisnode['min'])+";\n"
                        poriscinitstr += "\tpr"+parentNodeName+ "_" + nodename+".default_data = "+str(thisnode['default_data'])+";\n"
                        poriscinitstr += "\tpr"+parentNodeName+ "_" + nodename+".max = "+str(thisnode['max'])+";\n"                  
                        poriscinitstr += "\tpr"+parentNodeName+ "_" + nodename+".parent = &pr"+parentNodeName+";\n"
                        poriscinitstr += "\tpr"+parentNodeName+".values.push_back(&pr"+parentNodeName+ "_" + nodename+");\n"

                    else:
                        if thisclass == "prValText":
                            porishstr += "PORISValueText pr"+parentNodeName+ "_" + nodename+";\n"
                            '''
                            prShiftList_Normal.id = identcounter++;
                            prShiftList_Normal.idx = MyDASDevice::ShiftList_Normal;
                            prShiftList_Normal.ident = "ShiftList_Normal";
                            prShiftList_Normal.name = "ShiftList_Normal";
                            prShiftList_Normal.description = "Lista _separada por comas_ con los desplazamientos";
                            prShiftList_Normal.parent = &prShiftList;
                            '''                
                            poriscinitstr += "\n\tpr"+parentNodeName+ "_" + nodename+".id = identcounter++;\n"
                            poriscinitstr += "\tpr"+parentNodeName+ "_" + nodename+".idx = "+deviceName+"::"+parentNodeName+ "_" + nodename+";\n"
                            poriscinitstr += "\tpr"+parentNodeName+ "_" + nodename+".ident = \""+parentNodeName+ "_" + nodename+"\";\n"
                            poriscinitstr += "\tpr"+parentNodeName+ "_" + nodename+".name = \""+parentNodeName+ "_" + nodename+"\";\n"
                            poriscinitstr += "\tpr"+parentNodeName+ "_" + nodename+".description = \""+desctomonit(thisnode['description'])+"\";\n"
                            poriscinitstr += "\tpr"+parentNodeName+ "_" + nodename+".parent = &pr"+parentNodeName+";\n"
                            poriscinitstr += "\tpr"+parentNodeName+".values.push_back(&pr"+parentNodeName+ "_" + nodename+");\n"

                        else:
                            porishstr += "\t//TODO: Other pr"+parentNodeName+ "_" + nodename+"\n"


    filestr =  "// Created with PORIS @ which is Copyright (c) 2022 cosmoBots.eu\n"
    filestr += "// Do ethically correct things. Do not use our tools to do evil stuff\n"
    filestr += "// Think about enriching all humanity, besides yourself\n\n"

    filestr +="#include \"PORIS.h\"\n\n"
    filestr += "class "+deviceName+" {\n"
    filestr += magsstr+"\n"
    filestr += methodsstr+"\n"
    filestr += "}\n\n"

    with open("./"+deviceName+"/"+deviceName+".h", "w") as text_file:
        text_file.write(filestr)


    porishstr += "\nPORISSys *rootsys = NULL;\n\n"

    porishstr += "PORISSys *PORIS_init(void);\n"
    porishstr += "bool sync_PORIS_Model(void);\n\n"
    porishstr += "#endif\n"

    poriscinitstr += poriscinitrelstr + "\n" + poriscinitretstr + "}\n\n"
    poriscsyncstr += "\n\treturn true;\n}\n"

    poriscstr += poriscinitstr 
    poriscstr += poriscsyncstr

    with open("./"+deviceName+"/"+deviceName+"PORIS.py", "w+") as text_file:
        text_file.write(porishstr)
        text_file.write(poriscstr)



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

# Loads the ODS file into a nodes dictionary
nodes_dict = loadODS()

# Creates the code in the src_c++ folder
createCxxCode(nodes_dict,deviceName)
