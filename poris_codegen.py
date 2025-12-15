import os
import config


def nametoidl(n):
    ret = n.replace('(', '_')
    ret = ret.replace(')', '_')
    ret = ret.replace('.', '_')
    ret = ret.replace('+', 'p')
    ret = ret.replace('/', '_')
    ret = ret.replace('¿', '_')
    ret = ret.replace('?', '_')
    ret = ret.replace('-', '_')
    ret = ret.replace('á', 'a')
    ret = ret.replace('é', 'e')
    ret = ret.replace('í', 'i')
    ret = ret.replace('ó', 'o')
    ret = ret.replace('ú', 'u')
    ret = ret.replace('Á', 'A')
    ret = ret.replace('É', 'E')
    ret = ret.replace('Í', 'I')
    ret = ret.replace('Ó', 'O')
    ret = ret.replace('Ú', 'U')
    ret = ret.replace('ñ', 'ny')
    ret = ret.replace('Ñ', 'NY')

    if (ret.lower() == 'sequence'):
        ret = ret + "b"

    return ret


def desctomonit(n):
    return nametoidl(n.split('\n')[0].split('\r')[0])


def build_nodes_tree(nodes_dict, savemem=None):
    """Augment nodes dict with relationships, virtual/engineering nodes and return tree."""
    if savemem is None:
        savemem = config.savemem

    virtual_nodes_counter = 1
    nodes_to_add = {}

    # Parent relationship
    for thiskey in nodes_dict.keys():
        thisnode = nodes_dict[thiskey]

        if thisnode['parent'] is not None:
            parentkey = thisnode['parent']
            if len(parentkey) > 0:
                if parentkey in nodes_dict.keys():
                    thisparent = nodes_dict[parentkey]
                    thisnode['parentnode'] = thisparent
                    thisparent['children'].append(thiskey)

    # Create engineering modes
    if not savemem:
        for thiskey in nodes_dict.keys():
            thisnode = nodes_dict[thiskey]

            if thisnode['virtual'] == False:
                if thisnode['tracker'] == "prSys":
                    has_payload_child = False
                    for ch0 in thisnode['children']:
                        if ch0 in nodes_dict:
                            child = nodes_dict[ch0]
                            if child['tracker'] in ("prSys", "prParam", "prValue", "prValFloat", "prValText") and not child.get('virtual', False):
                                has_payload_child = True
                                break
                            if child['tracker'] == "prMode":
                                found = False
                                for b in child.get('blocking', []):
                                    if b in nodes_dict and nodes_dict[b]['tracker'] in ("prValue", "prValFloat", "prValText") and not nodes_dict[b].get('virtual', False):
                                        found = True
                                        break
                                if not found:
                                    for b in child.get('children', []):
                                        if b in nodes_dict and nodes_dict[b]['tracker'] in ("prValue", "prValFloat", "prValText") and not nodes_dict[b].get('virtual', False):
                                            found = True
                                            break
                                if found:
                                    has_payload_child = True
                                    break
                    if not has_payload_child:
                        continue

                    virtnode = {}
                    virtid = str(-virtual_nodes_counter)
                    virtual_nodes_counter += 1
                    virtident = "ENG" + virtid
                    virtnode['ident'] = virtident
                    virtnode['id'] = virtid
                    virtnode['tracker'] = "prMode"
                    virtnode['subject'] = "Engineering"
                    virtnode['description'] = thisnode['subject'] + " engineering mode"
                    virtnode['parent'] = thiskey
                    virtnode['parentnode'] = thisnode
                    virtnode['blocking'] = []
                    virtnode['precedents'] = []
                    virtnode['children'] = []
                    virtnode['virtual'] = False

                    # The engineering mode will be blocked by all the modes of its children
                    for ch0 in thisnode['children']:
                        if ch0 in nodes_dict and (nodes_dict[ch0]['tracker'] == "prSys" or nodes_dict[ch0]['tracker'] == "prParam"):
                            for ch in nodes_dict[ch0]['children']:
                                # If it is a virtual node, it can be not in nodes_dict, but in nodes_to_add
                                if ch in nodes_dict.keys():
                                    if nodes_dict[ch]['tracker'] == "prMode":
                                        if nodes_dict[ch]['virtual'] == False:
                                            virtnode['blocking'] += [ch]
                                else:
                                    if nodes_to_add[ch]['virtual'] == False:
                                        pass

                    if len(virtnode['blocking']) > 0:
                        nodes_to_add[virtident] = virtnode
                        thisnode['children'].append(virtident)

    tree_dict = {}
    while len(tree_dict) < len(nodes_dict):
        for k in nodes_dict.keys():
            if k not in tree_dict.keys():
                if 'parentnode' not in nodes_dict[k].keys():
                    tree_dict[k] = nodes_dict[k]
                else:
                    if nodes_dict[k]['parent'] in tree_dict.keys():
                        tree_dict[k] = nodes_dict[k]

    for n in nodes_to_add.keys():
        virtnode = nodes_to_add[n]
        thisparent = virtnode['parentnode']
        for c in thisparent['children']:
            if c != n and thisparent["tracker"] == "prSys":
                for c2 in tree_dict[c]['children']:
                    if c2 in nodes_to_add.keys():
                        virtnode['blocking'] += [c2]

    for n in nodes_to_add.keys():
        tree_dict[n] = nodes_to_add[n]

    return tree_dict


methods_dict = {}


def createPythonCode(nodes_dict, deviceName, output_path: str, relative_path: str):
    """Generate PORIS Python constructor code."""
    global methods_dict

    savemem = config.savemem

    methodsstr = "    #----------------------------------------------------------------------\n"
    methodsstr += "    #  Specific methods\n"
    methodsstr += "    #----------------------------------------------------------------------\n\n"
    porishstr = "from PORIS import *\n\n"
    porishstr += "class " + deviceName + "PORIS(PORISDoc):\n"
    porishstr += "    def __init__(self, project_id):\n"
    porishstr += "        super().__init__(project_id)\n"
    poriscstr = ""

    poriscinitstr = ""
    poriscinitrelstr = ""

    for thiskey in nodes_dict.keys():
        thisnode = nodes_dict[thiskey]
        nodename = nametoidl(thisnode['subject'])
        thisclass = thisnode['tracker']

        if thisclass == "prParam" or thisclass == "prSys":

            enumname = "enum_" + nodename
            enummodename = enumname + "Mode"
            choicesname = nodename + "ChoiceList"

            nodevar = "enum" + nodename
            modevar = "enum" + nodename + "Mode"

            modevar_ = modevar + "_"
            nodevar_ = nodevar + "_"

            if thisclass == "prParam":
                porishstr += "        self.pr" + nodename + " = PORISParam(\"" + nodename + "\")\n"

                methodsstr += "\n    ## " + thisclass + " " + nodename + " \n"
                methodsstr += "\n    # " + nodename + "\n"
                methodsstr += "    def get_" + nodename + "(self)-> PORISValue :\n"
                methodsstr += "        return self.pr" + nodename + ".getSelectedValue()\n\n"

                methodsstr += "    def set_" + nodename + "(self, value: PORISValue)-> PORISValue :\n"
                methodsstr += "        return self.pr" + nodename + ".setValue(value)\n\n"

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

                poriscinitstr += "        self.addItem(self.pr" + nodename + ")\n"
                if not savemem:
                    poriscinitstr += "        self.pr" + nodename + ".ident = \"" + thisnode['ident'] + "\"\n"
                    poriscinitstr += "        self.pr" + nodename + ".description = \"" + desctomonit(thisnode['description']) + "\"\n"

                if parentNode is not None:
                    poriscinitstr += "        self.sys" + parentNodeName + ".addParam(self.pr" + nodename + ")\n"

                methodsstr += "\n    ## " + nodename + "Mode \n"
                methodsstr += "    def get_" + nodename + "Mode(self)-> PORISMode:\n"
                methodsstr += "        return self.pr" + nodename + ".getSelectedMode()\n\n"

                methodsstr += "    def set_" + nodename + "Mode(self, mode: PORISMode)-> PORISMode :\n"
                methodsstr += "        return self.pr" + nodename + ".selectMode(mode)\n\n"

            else:
                porishstr += "        self.sys" + nodename + " = PORISSys(\"" + nodename + "\")\n"

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
                    porishstr += "        self.setRoot(self.sys" + nodename + ")\n"

                poriscinitstr += "        self.addItem(self.sys" + nodename + ")\n"
                if not savemem:
                    poriscinitstr += "        self.sys" + nodename + ".ident = \"" + thisnode['ident'] + "\"\n"
                    poriscinitstr += "        self.sys" + nodename + ".description = \"" + desctomonit(thisnode['description']) + "\"\n"

                if parentNode is not None:
                    poriscinitstr += "        self.sys" + parentNodeName + ".addSubsystem(self.sys" + nodename + ")\n"

                methodsstr += "\n    ## " + nodename + "Mode \n"
                methodsstr += "    def get_" + nodename + "Mode(self)-> PORISMode:\n"
                methodsstr += "        return self.sys" + nodename + ".getSelectedMode()\n\n"

                methodsstr += "    def set_" + nodename + "Mode(self, mode: PORISMode)-> PORISMode :\n"
                methodsstr += "        return self.sys" + nodename + ".selectMode(mode)\n\n"

            if thisclass == "prParam":
                valuesstr = ""
                valuesshortstr = ""
                valuemaxstr = valuesstr

            if not savemem:
                modeliststr = ""
            else:
                modeliststr = ""

            modeshortliststr = ""

            switchfm2 = False
            if 'parentnode' in thisnode.keys():
                parentnode = thisnode['parentnode']
                if parentnode is not None:
                    parentnodename = nametoidl(parentnode['subject'])
                    parentnodeclass = parentnode['tracker']
                    parentnodevar = "enum" + parentnodename
                    parentmodevar = "enum" + parentnodename + "Mode"
                    parentmodevar_ = parentmodevar + "_"
                    parentnodevar_ = parentnodevar + "_"
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
                                            poriscinitrelstr += "        # Marcamos " + nodename + "Mode_" + kvname + " como elegible para " + parentnodename + "Mode_" + childname + "\n"
                                            poriscinitrelstr += "        self.md" + parentnodename + "Mode_" + childname + ".addSubMode(self.md" + nodename + "Mode_" + kvname + ")\n"

                                        else:
                                            poriscinitrelstr += "        self.md" + parentnodename + childname + ".addSubMode(self.md" + nodename + kvname + ")\n"

                                        anyvaluepresentparentinner = True
                                        if not firstfound:
                                            firstfound = True

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
                            modeliststr += "," + nodename + "Mode_" + childname
                            modeshortliststr += "," + childname

                        else:
                            modeliststr += "," + nodename + childname
                            modeshortliststr += "," + childname

                        anyvaluepresentinner = False
                        firstdone = False

                        for kv in childnode['blocking']:
                            kvnode = nodes_dict[kv]
                            kvname = nametoidl(kvnode['subject'])
                            kvclass = kvnode['tracker']
                            if kvclass == "prValFloat" or kvclass == "prValText" or kvclass == "prValue":
                                if kvnode['virtual'] == False:
                                    if not savemem:
                                        poriscinitrelstr += "        # Marcamos " + nodename + "_" + kvname + " como elegible para " + nodename + "Mode_" + childname + "\n"
                                        poriscinitrelstr += "        self.md" + nodename + "Mode_" + childname + ".addValue(self.vl" + nodename + "_" + kvname + ")\n"

                                    else:
                                        poriscinitrelstr += "        self.md" + nodename + childname + ".addValue(self.vl" + nodename + "_" + kvname + ")\n"

                                anyvaluepresentinner = True
                                if not firstdone:
                                    firstdone = True

                                if kvclass == "prValFloat":
                                    if maximum_float is None:
                                        maximum_float = kvnode['max']
                                    else:
                                        maximum_float = max(maximum_float, kvnode['max'])

                                    if minimum_float is None:
                                        minimum_float = kvnode['min']
                                    else:
                                        minimum_float = min(minimum_float, kvnode['min'])

                                    methodsstrfl += "\n    ## " + thisclass + " " + parentNodeName + " \n"
                                    methodsstrfl += "\n    # " + nodename + "Double  \n"
                                    methodsstrfl += "    def get_" + nodename + "Double(self)-> float :\n"
                                    methodsstrfl += "        v = self.pr" + nodename + ".getSelectedValue()\n"
                                    methodsstrfl += "        v.__class__ = PORISValueFloat\n"
                                    methodsstrfl += "        return v.getData()\n\n"

                                    methodsstrfl += "    def set_" + nodename + "Double(self, data: float)-> float :\n"
                                    methodsstrfl += "        return self.pr" + nodename + ".getSelectedValue().setData(data)\n\n"

                                if kvclass == "prValText":
                                    methodsstrfl += "\n    ## " + thisclass + " " + parentNodeName + " \n"
                                    methodsstrfl += "\n    # " + nodename + "String #\n"
                                    methodsstrfl += "    def get_" + nodename + "String(self)-> str :\n"
                                    methodsstrfl += "        v = self.pr" + nodename + ".getSelectedValue()\n"
                                    methodsstrfl += "        v.__class__ = PORISValueString\n"
                                    methodsstrfl += "        return v.getData()\n\n"

                                    methodsstrfl += "    def set_" + nodename + "String(self, data: str)-> str :\n"
                                    methodsstrfl += "        return self.pr" + nodename + ".getSelectedValue().setData(data)\n\n"

                    else:
                        if childclass == "prValFloat" or childclass == "prValText" or childclass == "prValue":
                            valuesstr += "," + nodename + "_" + childname
                            valuesshortstr += "," + childname
                            valuemaxstr = nodename + "_" + childname

                methodsstr += methodsstrfl

            else:
                if thisclass == "prSys":
                    for k in thisnode['children']:
                        childnode = nodes_dict[k]
                        childname = nametoidl(childnode['subject'])
                        childclass = childnode['tracker']
                        if childclass == "prMode":
                            if not savemem:
                                modeliststr += "," + nodename + "Mode_" + childname
                                modeshortliststr += "," + childname

                            else:
                                modeliststr += "," + nodename + childname
                                modeshortliststr += "," + childname

        else:
            parentNode = thisnode['parentnode']
            parentNodeName = nametoidl(parentNode['subject'])
            if thisclass == "prMode":
                if not savemem:
                    porishstr += "        self.md" + parentNodeName + "Mode_" + nodename + " = PORISMode(\"" + parentNodeName + "Mode_" + nodename + "\")\n"

                else:
                    porishstr += "        self.md" + parentNodeName + nodename + " = PORISMode(\"" + nodename + "\")\n"

                if not savemem:
                    poriscinitstr += "        self.addItem(self.md" + parentNodeName + "Mode_" + nodename + ")\n"

                else:
                    poriscinitstr += "        self.addItem(self.md" + parentNodeName + "_" + nodename + ")\n"

                if not savemem:
                    poriscinitstr += "        self.md" + parentNodeName + "Mode_" + nodename + ".ident = \"" + thisnode['ident'] + "\"\n"
                    poriscinitstr += "        self.md" + parentNodeName + "Mode_" + nodename + ".description = \"" + desctomonit(thisnode['description']) + "\"\n"

                if parentNode['tracker'] == "prParam":
                    if not savemem:
                        poriscinitstr += "        self.pr" + parentNodeName + ".addMode(self.md" + parentNodeName + "Mode_" + nodename + ")\n"

                    else:
                        poriscinitstr += "        self.pr" + parentNodeName + ".addMode(self.md" + parentNodeName + nodename + ")\n"
                else:
                    if not savemem:
                        poriscinitstr += "        self.sys" + parentNodeName + ".addMode(self.md" + parentNodeName + "Mode_" + nodename + ")\n"

                    else:
                        poriscinitstr += "        self.sys" + parentNodeName + ".addMode(self.md" + parentNodeName + nodename + ")\n"

            else:
                if thisclass == "prValue":
                    if thisnode['virtual'] == False:
                        if not savemem:
                            porishstr += "        self.vl" + parentNodeName + "_" + nodename + " = PORISValue(\"" + parentNodeName + "_" + nodename + "\")\n"

                        else:
                            porishstr += "        self.vl" + parentNodeName + "_" + nodename + " = PORISValue(\"" + nodename + "\")\n"

                        poriscinitstr += "        self.addItem(self.vl" + parentNodeName + "_" + nodename + ")\n"

                        if not savemem:
                            poriscinitstr += "        self.vl" + parentNodeName + "_" + nodename + ".ident = \"" + thisnode['ident'] + "\"\n"
                            poriscinitstr += "        self.vl" + parentNodeName + "_" + nodename + ".description = \"" + desctomonit(thisnode['description']) + "\"\n"

                        poriscinitstr += "        self.pr" + parentNodeName + ".addValue(self.vl" + parentNodeName + "_" + nodename + ")\n"

                else:
                    if thisclass == "prValFloat":
                        if not savemem:
                            porishstr += "        self.vl" + parentNodeName + "_" + nodename + " = PORISValueFloat(\"" + parentNodeName + "_" + nodename + "\"," + str(thisnode['min']) + "," + str(thisnode['default_data']) + "," + str(thisnode['max']) + ")\n"

                        else:
                            porishstr += "        self.vl" + parentNodeName + "_" + nodename + " = PORISValueFloat(\"" + nodename + "\"," + str(thisnode['min']) + "," + str(thisnode['default_data']) + "," + str(thisnode['max']) + ")\n"

                        poriscinitstr += "        self.addItem(self.vl" + parentNodeName + "_" + nodename + ")\n"

                        if not savemem:
                            poriscinitstr += "        self.vl" + parentNodeName + "_" + nodename + ".ident = \"" + thisnode['ident'] + "\"\n"
                            poriscinitstr += "        self.vl" + parentNodeName + "_" + nodename + ".description = \"" + desctomonit(thisnode['description']) + "\"\n"

                        poriscinitstr += "        self.pr" + parentNodeName + ".addValue(self.vl" + parentNodeName + "_" + nodename + ")\n"

                    else:
                        if thisclass == "prValText":
                            if not savemem:
                                porishstr += "        self.vl" + parentNodeName + "_" + nodename + " = PORISValueString(\"" + parentNodeName + "_" + nodename + "\",'" + str(thisnode['deftext']) + "')\n"

                            else:
                                porishstr += "        self.vl" + parentNodeName + "_" + nodename + " = PORISValueString(\"" + nodename + "\",'" + str(thisnode['deftext']) + "')\n"

                            poriscinitstr += "        self.addItem(self.vl" + parentNodeName + "_" + nodename + ")\n"
                            if not savemem:
                                poriscinitstr += "        self.vl" + parentNodeName + "_" + nodename + ".ident = \"" + thisnode['ident'] + "\"\n"
                                poriscinitstr += "        self.vl" + parentNodeName + "_" + nodename + ".description = \"" + desctomonit(thisnode['description']) + "\"\n"

                            poriscinitstr += "        self.pr" + parentNodeName + ".addValue(self.vl" + parentNodeName + "_" + nodename + ")\n"

                        else:
                            if thisclass == "prCmd":
                                thisnode_tmp = {}
                                thiskey_tmp = parentNodeName + "_" + nodename
                                thisnode_tmp['method'] = "exec" + thiskey_tmp
                                thisnode_tmp['node'] = parentNodeName
                                methods_dict[thiskey_tmp] = thisnode_tmp
                                methodsstr += '\n    ## Action trigger ' + thiskey_tmp + ' ##\n'
                                methodsstr += '    def ' + thisnode_tmp['method'] + '(self, value: bool) -> bool:\n'
                                methodsstr += '        # Override this\n'
                                methodsstr += '        return True\n\n'

                            else:
                                porishstr += "        //TODO: Other xx" + parentNodeName + "_" + nodename + "\n"

    poriscinitstr += poriscinitrelstr + "\n"

    poriscstr += poriscinitstr

    dest_dir = os.path.join(output_path, relative_path.lstrip("/"))
    os.makedirs(dest_dir, exist_ok=True)
    with open(os.path.join(dest_dir, f"{deviceName}PORIS.py"), "w+") as text_file:
        text_file.write(porishstr)
        text_file.write(poriscstr)
        text_file.write(methodsstr)
