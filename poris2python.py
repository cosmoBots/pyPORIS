# Importing auxiliar libraries for the test
import argparse                     # This library allows us to easily parse the command line arguments

from pyexcel_ods import get_data    # This function allows us to easily read an ODS file (for api)
from xml.dom import minidom
from pathlib import Path
import os

# Importing test configuration file
import config

savemem = config.savemem

def nametoidl(n):
    ret = n.replace('(','_')
    ret = ret.replace(')','_')
    ret = ret.replace('.','_')
    ret = ret.replace('+','p')
    ret = ret.replace('/','_')
    ret = ret.replace('¿','_')    
    ret = ret.replace('?','_')    
    ret = ret.replace('-','_')
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

def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

parser = argparse.ArgumentParser(description='Launches a PORIS device generation from an ODS file describing the PORIS instrument')

## The second argument is the api ODS file
parser.add_argument('model_root_path',type=dir_path, help="the root path where the models shall be picket from")
parser.add_argument('model_path',type=argparse.FileType('r'), help="the path for the model to be processed")
parser.add_argument('output_path',type=dir_path, help="the path to create the Python classes")

# Obtaining the arguments from the command line
args=parser.parse_args()

# Printing the obtained arguments:
print("/* The PORIS instrument description ODS filename is:",args.model_path.name+" */")
deviceName = Path(args.model_path.name).stem
print("Device name:",deviceName)

relativepath = args.model_path.name.replace(args.model_root_path, '', 1)
relativepath = ''.join(relativepath.rsplit(".ods", 1))

# As an example of a constant defined in the configuration file, we'll print the welcome message
print(config.welcome_message)

def loadODS():

    dictdata = get_data(args.model_path.name,start_row=config.dict_max_rows_row, row_limit=config.dict_max_rows_row+1, 
        start_column=config.dict_max_rows_column,column_limit=config.dict_max_rows_column)[config.dict_file_sheet]

    desc_file_row_limit = dictdata[0][1]
    # Now we read the PORIS instrument description from the file file
    filedata = get_data(args.model_path.name,start_row=config.desc_file_start_row, row_limit=desc_file_row_limit, 
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

    nodes_to_add = {}
    if not savemem:
        # Create engineering modes
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
                                # If it is a virtual node, it can be not in nodes_dict, but in nodes_to_add
                                if ch in nodes_dict.keys():
                                    if nodes_dict[ch]['tracker'] == "prMode":
                                        if nodes_dict[ch]['virtual'] == False:
                                            virtnode['blocking'] += [ch]
                                            print(ch,nodes_dict[ch]['subject'],"bloquea a",virtident,virtnode['description'])
                                            #print(virtnode['blocking'])
                                
                                else:
                                    if nodes_to_add[ch]['virtual'] == False:
                                        print("CHECK THIS: A NON VIRTUAL NODE NOT IN NODES_DICT")


                    if len(virtnode['blocking']) > 0:
                        nodes_to_add[virtident] = virtnode
                        thisnode['children'].append(virtident)

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



# This function will create, in parallel:
# - The $S1.py
# - The $S1PORIS.py

methods_dict = {}

def createPythonCode(nodes_dict,deviceName,output_path: str,relative_path: str):
    global methods_dict

    methodsstr =  "    #----------------------------------------------------------------------\n"
    methodsstr += "    #  Specific methods\n"
    methodsstr += "    #----------------------------------------------------------------------\n\n"
    porishstr =  "from PORIS import *\n\n"
    porishstr += "class "+deviceName+"PORIS(PORISDoc):\n"
    porishstr += "    def __init__(self, project_id):\n"
    porishstr += "        super().__init__(project_id)\n"
    poriscstr =  ""

    poriscinitstr = ""
    poriscinitrelstr = ""


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
                porishstr += "        self.pr"+nodename+" = PORISParam(\""+nodename+"\")\n"
                if not savemem:
                    porishstr += "        self.md"+nodename+"Mode_UNKNOWN = PORISMode(\""+nodename+"Mode_UNKNOWN\")\n"
                    porishstr += "        self.vl"+nodename+"_UNKNOWN = PORISValue(\""+nodename+"_UNKNOWN\")\n"

                else:
                    porishstr += "        self.md"+nodename+"UNKNOWN = PORISMode(\"UNKNOWN\")\n"
                    porishstr += "        self.vl"+nodename+"_UNKNOWN = PORISValue(\"UNKNOWN\")\n"


                methodsstr += "\n    ## "+thisclass+" "+nodename+" \n"
                methodsstr += "\n    # "+nodename+"\n"
                methodsstr += "    def get_"+nodename+"(self)-> PORISValue :\n"
                methodsstr += "        return self.pr"+nodename+".getSelectedValue()\n\n"

                methodsstr += "    def set_"+nodename+"(self, value: PORISValue)-> PORISValue :\n"
                methodsstr += "        return self.pr"+nodename+".setValue(value)\n\n"

                '''
                prBinning.id = idcounter++;
                prBinning.idx = 1;
                prBinning.ident = "Binning";
                prBinning.name = "Binning";
                prBinning.description = "Parametro de binning";
                prBinning.parent = &prDetector;
                prDetector.params.push_back(&prBinning);

                prBinning_UNKNOWN.id = idcounter++;
                prBinning_UNKNOWN.idx = MyDASDevice::Binning_UNKNOWN;
                prBinning_UNKNOWN.ident = "Binning_UNKNOWN";
                prBinning_UNKNOWN.name = "Binning_UNKNOWN";
                prBinning_UNKNOWN.description = "Binning_UNKNOWN";
                prBinning_UNKNOWN.parent = &prBinning;
                prBinning.values.push_back(&prBinning_UNKNOWN);

                prBinningMode_UNKNOWN.id = idcounter++;
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

                poriscinitstr += "        self.addItem(self.pr"+nodename+")\n"
                if not savemem:
                    poriscinitstr += "        self.pr"+nodename+".ident = \""+nodename+"\"\n"
                    poriscinitstr += "        self.pr"+nodename+".description = \""+desctomonit(thisnode['description'])+"\"\n"
                
                if parentNode is not None:
                    poriscinitstr += "        self.sys"+parentNodeName+".addParam(self.pr"+nodename+")\n"

                if not savemem:
                    poriscinitstr += "        self.addItem(self.vl"+nodename+"_UNKNOWN)\n"
                    
                
                if not savemem:
                    poriscinitstr += "        self.vl"+nodename+ "_UNKNOWN.ident = \""+nodename+ "_UNKNOWN\"\n"
                    poriscinitstr += "        self.vl"+nodename+ "_UNKNOWN.description = \"Unknown value for "+nodename+"\"\n"
                
                poriscinitstr += "        self.pr"+nodename+".addValue(self.vl"+nodename+ "_UNKNOWN)\n"

                if not savemem:
                    poriscinitstr += "        self.addItem(self.md"+nodename+"Mode_UNKNOWN)\n"
                else:
                    poriscinitstr += "        self.addItem(self.md"+nodename+"UNKNOWN)\n"

                if not savemem:
                    poriscinitstr += "        self.md"+nodename+ "Mode_UNKNOWN.ident = \""+nodename+ "Mode_UNKNOWN\"\n"
                    poriscinitstr += "        self.md"+nodename+ "Mode_UNKNOWN.description = \"Unknown mode for "+nodename+"\"\n"
                
                if not savemem:
                    poriscinitstr += "        self.pr"+nodename+".addMode(self.md"+nodename+ "Mode_UNKNOWN)\n"
                    poriscinitstr += "        self.md"+nodename+ "Mode_UNKNOWN.addValue(self.vl"+nodename+ "_UNKNOWN)\n"
                    poriscinitstr += "        self.md"+parentNodeName+ "Mode_UNKNOWN.addSubMode(self.md"+nodename+ "Mode_UNKNOWN)\n"

                else:
                    poriscinitstr += "        self.pr"+nodename+".addMode(self.md"+nodename+ "UNKNOWN)\n"
                    poriscinitstr += "        self.md"+nodename+ "UNKNOWN.addValue(self.vl"+nodename+ "_UNKNOWN)\n"
                    poriscinitstr += "        self.md"+parentNodeName+ "UNKNOWN.addSubMode(self.md"+nodename+ "UNKNOWN)\n"

                methodsstr += "\n    ## "+nodename+"Mode \n"
                methodsstr += "    def get_"+nodename+"Mode(self)-> PORISMode:\n"
                #return self.sysARCGenIII.getSelectedMode()
                methodsstr += "        return self.pr"+nodename+".getSelectedMode()\n\n"

                methodsstr += "    def set_"+nodename+"Mode(self, mode: PORISMode)-> PORISMode :\n"
                methodsstr += "        return self.pr"+nodename+".selectMode(mode)\n\n"                    

            else:
                # PORISSys prDetector;
                porishstr += "        self.sys"+nodename+" = PORISSys(\""+nodename+"\")\n"
                if not savemem:
                    porishstr += "        self.md"+nodename+"Mode_UNKNOWN = PORISMode(\""+nodename+"Mode_UNKNOWN\")\n"

                else:
                    porishstr += "        self.md"+nodename+"UNKNOWN = PORISMode(\"UNKNOWN\")\n"

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
                    porishstr += "        self.setRoot(self.sys"+nodename+")\n"
                    

                '''
                prDetector.id = idcounter++;
                prDetector.idx = 0;
                prDetector.ident = "Detector";
                prDetector.name = "Detector";
                prDetector.description = "Detector";
                prDetector.parent = NULL;
                '''
                poriscinitstr += "        self.addItem(self.sys"+nodename+")\n"                
                if not savemem:
                    poriscinitstr += "        self.sys"+nodename+".ident = \""+nodename+"\"\n"
                    poriscinitstr += "        self.sys"+nodename+".description = \""+desctomonit(thisnode['description'])+"\"\n"
                
                if parentNode is not None:
                    poriscinitstr += "        self.sys"+parentNodeName+".addSubsystem(self.sys"+nodename+")\n" 

                if not savemem:
                    poriscinitstr += "        self.addItem(self.md"+nodename+"Mode_UNKNOWN)\n"

                else:
                    poriscinitstr += "        self.addItem(self.md"+nodename+"UNKNOWN)\n"
                    

                if not savemem:
                    poriscinitstr += "        self.md"+nodename+ "Mode_UNKNOWN.ident = \""+nodename+ "Mode_UNKNOWN\"\n"
                    poriscinitstr += "        self.md"+nodename+ "Mode_UNKNOWN.description = \""+desctomonit(thisnode['description'])+"\"\n"
                    poriscinitstr += "        self.sys"+nodename+".addMode(self.md"+nodename+ "Mode_UNKNOWN)\n"

                else:
                    poriscinitstr += "        self.sys"+nodename+".addMode(self.md"+nodename+ "UNKNOWN)\n"

                methodsstr += "\n    ## "+nodename+"Mode \n"
                methodsstr += "    def get_"+nodename+"Mode(self)-> PORISMode:\n"
                #return self.sysARCGenIII.getSelectedMode()
                methodsstr += "        return self.sys"+nodename+".getSelectedMode()\n\n"

                methodsstr += "    def set_"+nodename+"Mode(self, mode: PORISMode)-> PORISMode :\n"
                methodsstr += "        return self.sys"+nodename+".selectMode(mode)\n\n"                
            


            if thisclass == "prParam":
                valuesstr = nodename+"_UNKNOWN"
                valuesshortstr = "UNKNOWN"
                valuemaxstr = valuesstr
            
            if not savemem:
                modeliststr = nodename+"Mode_UNKNOWN"
            
            else:
                modeliststr = nodename+"UNKNOWN"
                
            modeshortliststr = "UNKNOWN"
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

                    for k in parentnode['children']:
                        childnode = nodes_dict[k]
                        childname = nametoidl(childnode['subject'])
                        childclass = childnode['tracker']
                        if childclass == "prMode":
                            anyvaluepresentparentinner = False
                            firstfound = False                        
                            
                            for kv in childnode['blocking']:
                                kvnode = nodes_dict[kv]
                                kvname = nametoidl(kvnode['subject'])
                                kvclass = kvnode['tracker']
                                if kvclass == "prMode":
                                    if kvnode['parentnode'] == thisnode:                                     
                                        if not savemem:
                                            poriscinitrelstr += "        # Marcamos "+nodename+"Mode_"+kvname+" como elegible para "+parentnodename+"Mode_"+childname+"\n"
                                            poriscinitrelstr += "        self.md"+parentnodename+"Mode_"+childname+".addSubMode(self.md"+nodename+"Mode_"+kvname+")\n"
                                        
                                        else:
                                            poriscinitrelstr += "        self.md"+parentnodename+childname+".addSubMode(self.md"+nodename+kvname+")\n"

                                        anyvaluepresentparentinner = True
                                        if not firstfound:
                                            firstfound = True

                            if (anyvaluepresentparentinner):
                                anyvaluepresentparentouter = True


            else:
                parentnode = None

            monitsetparam = None
            methodsstrfl = ""
            minimum_float = None
            maximum_float = None
            if thisclass == "prParam":
                for k in thisnode['children']:
                    childnode = nodes_dict[k]
                    childname = nametoidl(childnode['subject'])
                    childclass = childnode['tracker']
                    if childclass == "prMode":
                        if not savemem:
                            modeliststr += ","+nodename+"Mode_"+childname
                            modeshortliststr += ","+childname
                            
                        else:
                            modeliststr += ","+nodename+childname
                            modeshortliststr += ","+childname


                        anyvaluepresentinner = False
                        firstdone = False

                        for kv in childnode['blocking']:
                            kvnode = nodes_dict[kv]
                            kvname = nametoidl(kvnode['subject'])
                            kvclass = kvnode['tracker']
                            if kvclass == "prValFloat" or kvclass == "prValText" or kvclass == "prValue":                               
                                if kvnode['virtual'] == False:
                                    if not savemem:
                                        poriscinitrelstr += "        # Marcamos "+nodename+"_"+kvname+" como elegible para "+nodename+"Mode_"+childname+"\n"
                                        poriscinitrelstr += "        self.md"+nodename+"Mode_"+childname+".addValue(self.vl"+nodename+"_"+kvname+")\n"

                                    else:
                                        poriscinitrelstr += "        self.md"+nodename+childname+".addValue(self.vl"+nodename+"_"+kvname+")\n"

                                anyvaluepresentinner = True
                                if not firstdone:
                                    firstdone = True

                                if kvclass == "prValFloat":
                                    if maximum_float is None:
                                        maximum_float = kvnode['max']
                                    else:
                                        maximum_float = max(maximum_float,kvnode['max'])

                                    if minimum_float is None:
                                        minimum_float = kvnode['min']
                                    else:
                                        minimum_float = min(minimum_float,kvnode['min'])

                                    methodsstrfl += "\n    ## "+thisclass+" "+parentNodeName+" \n"
                                    methodsstrfl += "\n    # "+nodename+"Double  \n"
                                    methodsstrfl += "    def get_"+nodename+"Double(self)-> float :\n"
                                    methodsstrfl += "        v = self.pr"+nodename+".getSelectedValue()\n"
                                    methodsstrfl += "        v.__class__ = PORISValueFloat\n"
                                    methodsstrfl += "        return v.getData()\n\n"

                                    methodsstrfl += "    def set_"+nodename+"Double(self, data: float)-> float :\n"
                                    methodsstrfl += "        return self.pr"+nodename+".getSelectedValue().setData(data)\n\n"

                                if kvclass == "prValText":
                                    methodsstrfl += "\n    ## "+thisclass+" "+parentNodeName+" \n"
                                    methodsstrfl += "\n    # "+nodename+"String #\n"
                                    methodsstrfl += "    def get_"+nodename+"String(self)-> str :\n"
                                    methodsstrfl += "        v = self.pr"+nodename+".getSelectedValue()\n"
                                    methodsstrfl += "        v.__class__ = PORISValueString\n"
                                    methodsstrfl += "        return v.getData()\n\n"

                                    methodsstrfl += "    def set_"+nodename+"String(self, data: str)-> str :\n"
                                    methodsstrfl += "        return self.pr"+nodename+".getSelectedValue().setData(data)\n\n"

                    else:
                        if childclass == "prValFloat" or childclass == "prValText" or childclass == "prValue":
                            valuesstr += ","+nodename+"_"+childname
                            valuesshortstr += ","+childname
                            valuemaxstr = nodename+"_"+childname

                methodsstr += methodsstrfl

            else:
                if thisclass == "prSys":
                    for k in thisnode['children']:
                        childnode = nodes_dict[k]
                        childname = nametoidl(childnode['subject'])
                        childclass = childnode['tracker']
                        if childclass == "prMode":
                            if not savemem:
                                modeliststr += ","+nodename+"Mode_"+childname
                                modeshortliststr += ","+childname

                            else:
                                modeliststr += ","+nodename+childname
                                modeshortliststr += ","+childname


        else:
            parentNode = thisnode['parentnode']
            parentNodeName = nametoidl(parentNode['subject'])
            if thisclass == "prMode":
                #PORISMode prDetectorMode_Image;
                if not savemem:
                    porishstr += "        self.md"+parentNodeName+ "Mode_" + nodename+" = PORISMode(\""+parentNodeName+ "Mode_" + nodename + "\")\n"

                else:
                    porishstr += "        self.md"+parentNodeName + nodename+" = PORISMode(\"" + nodename + "\")\n"

                '''
                prDetectorMode_UNKNOWN.id = idcounter++;
                prDetectorMode_UNKNOWN.idx = MyDASDevice::DetectorMode_UNKNOWN;
                prDetectorMode_UNKNOWN.ident = "DetectorMode_UNKNOWN";
                prDetectorMode_UNKNOWN.name = "DetectorMode_UNKNOWN";
                prDetectorMode_UNKNOWN.description = "DetectorMode_UNKNOWN";
                prDetectorMode_UNKNOWN.parent = &prDetector;
                '''
                if not savemem:
                    poriscinitstr += "        self.addItem(self.md"+parentNodeName+ "Mode_"+nodename+")\n"

                else:
                    poriscinitstr += "        self.addItem(self.md" + parentNodeName + "_" + nodename+")\n"

                if not savemem:
                    poriscinitstr += "        self.md"+parentNodeName+ "Mode_" + nodename+".ident = \""+parentNodeName+ "Mode_" + nodename+"\"\n"
                    poriscinitstr += "        self.md"+parentNodeName+ "Mode_" + nodename+".description = \""+desctomonit(thisnode['description'])+"\"\n"

                if parentNode['tracker'] == "prParam":
                    if not savemem:
                        poriscinitstr += "        self.pr"+parentNodeName+".addMode(self.md"+parentNodeName+ "Mode_" + nodename+")\n"

                    else:
                        poriscinitstr += "        self.pr"+parentNodeName+".addMode(self.md"+parentNodeName+ nodename+")\n"
                else:
                    if not savemem:
                        poriscinitstr += "        self.sys"+parentNodeName+".addMode(self.md"+parentNodeName+ "Mode_" + nodename+")\n"

                    else:
                        poriscinitstr += "        self.sys"+parentNodeName+".addMode(self.md"+parentNodeName + nodename+")\n"

            else:
                if thisclass == "prValue":
                    if thisnode['virtual'] == False:
                        #PORISValue prBinning_1x1;
                        if not savemem:
                            porishstr += "        self.vl"+parentNodeName+"_" + nodename+" = PORISValue(\""+parentNodeName+"_" + nodename+"\")\n"

                        else:
                            porishstr += "        self.vl"+parentNodeName+"_" + nodename+" = PORISValue(\"" + nodename+"\")\n"

                        '''
                        prBinning_1x1.id = idcounter++;
                        prBinning_1x1.idx = MyDASDevice::Binning_1x1;
                        prBinning_1x1.ident = "Binning_1x1";
                        prBinning_1x1.name = "Binning_1x1";
                        prBinning_1x1.description = "Sin binning";
                        prBinning_1x1.parent = &prBinning;
                        '''                
                        poriscinitstr += "        self.addItem(self.vl" + parentNodeName+ "_"  + nodename+")\n"

                        if not savemem:
                            poriscinitstr += "        self.vl"+parentNodeName+ "_" + nodename+".ident = \""+parentNodeName+ "_" + nodename+"\"\n"
                            poriscinitstr += "        self.vl"+parentNodeName+ "_" + nodename+".description = \""+desctomonit(thisnode['description'])+"\"\n"
                        
                        poriscinitstr += "        self.pr"+parentNodeName+".addValue(self.vl"+parentNodeName+ "_" + nodename+")\n"

                else:
                    if thisclass == "prValFloat":             
                        #PORISValueFloat prExpTime_Normal;
                        if not savemem:
                            porishstr += "        self.vl"+parentNodeName+"_" + nodename+" = PORISValueFloat(\""+parentNodeName+"_" + nodename + "\","+str(thisnode['min'])+","+str(thisnode['default_data'])+","+str(thisnode['max'])+")\n"

                        else:
                            porishstr += "        self.vl"+parentNodeName+"_" + nodename+" = PORISValueFloat(\"" + nodename + "\","+str(thisnode['min'])+","+str(thisnode['default_data'])+","+str(thisnode['max'])+")\n"

                        '''
                        prExpTime_Normal.id = idcounter++;
                        prExpTime_Normal.idx = MyDASDevice::ExpTime_Normal;
                        prExpTime_Normal.ident = "ExpTime_Normal";
                        prExpTime_Normal.name = "ExpTime_Normal";
                        prExpTime_Normal.description = "Rango normal de valores para ExpTime";
                        prExpTime_Normal.parent = &prExpTime;                    
                        '''                
                        poriscinitstr += "        self.addItem(self.vl" + parentNodeName + "_" + nodename+")\n"

                        if not savemem:
                            poriscinitstr += "        self.vl"+parentNodeName+ "_" + nodename+".ident = \""+parentNodeName+ "_" + nodename+"\"\n"
                            poriscinitstr += "        self.vl"+parentNodeName+ "_" + nodename+".description = \""+desctomonit(thisnode['description'])+"\"\n"
                        
                        #poriscinitstr += "        self.vl"+parentNodeName+ "_" + nodename+".min = "+str(thisnode['min'])+"\n"
                        #poriscinitstr += "        self.vl"+parentNodeName+ "_" + nodename+".default_data = "+str(thisnode['default_data'])+"\n"
                        #poriscinitstr += "        self.vl"+parentNodeName+ "_" + nodename+".max = "+str(thisnode['max'])+"\n"                  
                        poriscinitstr += "        self.pr"+parentNodeName+".addValue(self.vl"+parentNodeName+ "_" + nodename+")\n"

                    else:
                        if thisclass == "prValText":
                            if not savemem:
                                porishstr += "        self.vl"+parentNodeName+"_" + nodename+" = PORISValueString(\""+parentNodeName+"_" + nodename+"\",'"+str(thisnode['deftext'])+"')\n"

                            else:
                                porishstr += "        self.vl"+parentNodeName+"_" + nodename+" = PORISValueString(\""+nodename+"\",'"+str(thisnode['deftext'])+"')\n"

                            '''
                            prShiftList_Normal.id = idcounter++;
                            prShiftList_Normal.idx = MyDASDevice::ShiftList_Normal;
                            prShiftList_Normal.ident = "ShiftList_Normal";
                            prShiftList_Normal.name = "ShiftList_Normal";
                            prShiftList_Normal.description = "Lista _separada por comas_ con los desplazamientos";
                            prShiftList_Normal.parent = &prShiftList;
                            '''                
                            poriscinitstr += "        self.addItem(self.vl" + parentNodeName + "_" + nodename+")\n"
                            if not savemem:
                                poriscinitstr += "        self.vl"+parentNodeName+ "_" + nodename+".ident = \""+parentNodeName+ "_" + nodename+"\"\n"
                                poriscinitstr += "        self.vl"+parentNodeName+ "_" + nodename+".description = \""+desctomonit(thisnode['description'])+"\"\n"
                            
                            poriscinitstr += "        self.pr"+parentNodeName+".addValue(self.vl"+parentNodeName+ "_" + nodename+")\n"

                        else:
                            if thisclass == "prCmd":
                                thisnode = {}
                                thiskey = parentNodeName+ "_" + nodename
                                thisnode['method'] = "exec"+thiskey
                                thisnode['node'] = parentNodeName
                                methods_dict[thiskey] = thisnode
                                methodsstr += '\n    ## Action trigger '+thiskey+' ##\n'
                                methodsstr += '    def '+thisnode['method']+'(self, value: bool) -> bool:\n'
                                methodsstr += '        # Override this\n'
                                methodsstr += '        return True\n\n'

                            else:                            
                                porishstr += "        //TODO: Other xx"+parentNodeName+ "_" + nodename+"\n"

    poriscinitstr += poriscinitrelstr + "\n"
    
    poriscstr += poriscinitstr 
    
    with open("./"+output_path+relative_path+"/"+deviceName+"PORIS.py", "w+") as text_file:
        text_file.write(porishstr)
        text_file.write(poriscstr)
        text_file.write(methodsstr)

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
createPythonCode(nodes_dict,deviceName,args.output_path, relativepath)
