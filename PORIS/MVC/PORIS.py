from Model import Model
from Observer import Observer
from xml.dom import minidom
import Utils

class PORISNode:
    pass

class PORISAttribute:
    pass

class PORIS:
    pass


class PORIS(Model):

    __instanceList = []
    __xmlLoaderHashMap = {}
      
    def __init__(self, name: str):
        super().__init__(name)
        self.__destinations = []
        self.__sources = []
        self.__label = name
        self.__attributes = []
        self.__id = None
        self.__nodeTypeId = None
        self.__modeVisibleFlag = False
        self.__class__.__instanceList.append(self)


    def getAttributes(self) -> PORISAttribute:
        return self.__attributes


    def addAttribute(self, attr: PORISAttribute):
        ret = False
        if attr not in self.__attributes:
            self.__attributes.append(attr)
            ret = True
            self.notifyObs()

        return ret


    def getId(self) -> int:
        return self.__id
    

    def setId(self, id: int):
        self.__id = id
        self.notifyObs()


    def getNodeTypeId(self) -> int:
        return self.__nodeTypeId
    

    def setNodeTypeId(self, id: int):
        self.__nodeTypeId = id
        self.notifyObs()


    def isModeVisibleFlag(self) -> bool:
        return self.__modeVisibleFlag


    def getLabel(self) -> str:
        return self.__label
    

    def setLabel(self, label: str):
        self.__label = label
        self.notifyObs()


    def toString(self) -> str:
        return self.getLabel()


    def attach(self, obs: Observer):
        super().attach(obs)
        for d in self.__destinations:
            d.attach(obs)


    def addDestination(self, child: PORIS):
        if child not in self.__destinations:
            self.__destinations.append(child)
            if self not in child.__sources:
                child.__sources.append(self)

            self.notifyObs()


    def addSource(self, parent: PORIS):
        if parent not in self.__sources:
            self.__sources.append(parent)
            if self not in parent.__destinations:
                parent.__destinations.append(self)

            self.notifyObs()


    def isValidFromStr(self, name: str) -> bool:
        return self.getName() == name
    

    def getDestinations(self):
        return self.__destinations
    

    def getDestinationFromName(self, name:str) -> PORIS:
        for d in self.__destinations:
            if d.isValidFromStr(name):
                return d
            
        return None


    def getDestinationFromName(self, name:str) -> PORIS:
        for d in self.__destinations:
            if d.isValidFromStr(name):
                return d
            
        return None


    def getSourceFromName(self, name:str) -> PORIS:
        for s in self.__sources:
            if s.isValidFromStr(name):
                return s
            
        return None


    def isConsistent(self) -> bool:
        # In Python we do not have to worry about this, but...
        return (self.__destinations is not None) and (self.__sources is not None)


    def subTree(self, list) -> bool:
        ret = True
        if self not in list:
            for d in self.__destinations:
                ret = ret and d.subTree(list)

            if ret:
                ret = list.append(self)

        return ret

    @classmethod
    def createInstanceOfClass(cls, clase, instanceName: bool) -> PORIS:
        return clase(instanceName)


    def isXMLExportable(self):
        return True


    def toXML(self, doc: minidom.Document, onlyIdent: bool) -> minidom.Element:
        if self.isConsistent():
            ret = doc.createElement(self.__class__.__name__)
            nameNode = doc.createElement("name")
            Utils.setTextContent(doc, nameNode,self.getName())
            ret.appendChild(nameNode)
            if not onlyIdent:
                idNode = doc.createElement("id")
                idNode.setAttribute("type","integer")
                Utils.setTextContent(doc, idNode, str(self.getId()))
                ret.appendChild(idNode)
                typeNode = doc.createElement("type")
                Utils.setTextContent(doc, typeNode, self.__class__.__name__)
                ret.appendChild(typeNode)
                nodeTypeIdNode = doc.createElement("node-type-id")
                Utils.setTextContent(doc, nodeTypeIdNode, str(self.getNodeTypeId()))
                ret.appendChild(nodeTypeIdNode)                

                labelsNode = doc.createElement("labels")
                labelsNode.setAttribute("type","array")
                if not self.getLabel() == self.getName():
                    labelNode = doc.createElement("label")
                    # Name
                    labelNameNode = doc.createElement("name")
                    Utils.setTextContent(doc, labelNameNode, señf.getLabel())
                    labelNode.appendChild(labelNameNode)
                    # Scope
                    labelScopeNode = doc.createElement("scope-kind")
                    labelScopeOPMSNode = doc.createElement("name")
                    Utils.setTextContent(doc, labelScopeOPMSNode, "OPMS")
                    labelScopeNode.appendChild(labelScopeOPMSNode)
                    labelNode.appendChild(labelScopeNode)

                    labelsNode.appendChild(labelNode)

                ret.appendChild(labelsNode)


                destsNode = doc.createElement("destinations")
                destsNode.setAttribute("type", "array")
                for d in self.__destinations:
                    if d.isXMLExportable():
                        destNode = doc.createElement("destination")
                        destNode.setAttribute("type", d.__class__.__name__)
                        destIdNode = doc.createElement("id")
                        destIdNode.setAttribute("type", "integer")
                        Utils.setTextContent(doc, destIdNode, str(d.getId()))
                        destNode.appendChild(destIdNode)
                        destsNode.appendChild(destNode)


                ret.appendChild(destsNode)

                attrsNode = doc.createElement("node-attributes")
                attrsNode.setAttribute("type", "array")
                for a in self.__attributes:
                    attrNode = doc.createElement("node-attribute")
                    attrNameNode = doc.createElement("name")
                    Utils.setTextContent(doc, attrNameNode, a.getName())
                    attrNode.appendChild(attrNameNode)
                    attrContentNode = doc.createElement("content")
                    Utils.setTextContent(doc, attrContentNode, a.getContent())
                    attrNode.appendChild(attrContentNode)
                    attrsNode.appendChild(attrNode)

                ret.appendChild(attrsNode)

            return ret
        
        else:
            print("ERROR: Basemodel",self.toString(), "is not consistent:")
            print("    PORIS node has the following destinations",self.__destinations)
            for d in self.__destinations:
                print("Value",d.toString(),"is consistent?",d.isConsistent())
            
            print("    PORIS node has the following sources",self.__sources)
            for s in self.__sources:
                print("Value",s.toString(),"is consistent?",s.isConsistent())
            return None



    @classmethod
    def getChildNodeWithName(node: minidom.Node, name: str) -> minidom.Node:
        childNodes = node.getChildNodes()

        for c in childNodes:
            if c.getNodeName() == name:
                return c


    def getFromListByClass(list, cls):
        ret = []
        for l in list:
            if l.isDescendantOf(cls):
                ret.append(l)

        return ret
    

    def getFromListByClassAndName(list, cls, name: str) -> PORIS:
        for l in list:
            if l.isDescendantOf(cls):
                if l.getName == name:
                    return l

        return None
        

    def loadFromXML(self, node: minidom.Node) -> bool:
        ret = True

        instanceName = Utils.getTextContent(PORIS.getChildNodeWithName(node, "name"))
        self.setName(instanceName)
        self.setLabel(instanceName)

        instanceId = int(Utils.getTextContent(PORIS.getChildNodeWithName(node, "id")))
        self.setId(instanceId)
        self.__xmlLoaderHashMap[instanceId] = self

        instanceNodeTypeId = int(Utils.getTextContent(PORIS.getChildNodeWithName(node, "node-type-id")))
        self.setNodeTypeId(instanceNodeTypeId)

        labelsNode = PORIS.getChildNodeWithName(node, "labels")
        if (labelsNode is not None):
            childLabels = labelsNode.chilNodes
            for labelNode in childLabels:
                if labelNode.getNodeName() =="label":
                    scopeNode = PORIS.getChildNodeWithName(labelNode, "scope-kind")
                    if (scopeNode is not None):
                        scopeNameNode = PORIS.getChildNodeWithName(scopeNode, "name")
                        scopeName = Utils.getTextContent(scopeNameNode)
                        if (scopeName == "CfgPanel"):
                            self.setLabel(Utils.getTextContent(PORIS.getChildNodeWithName(labelNode,"name")))
        
        attrsNode = PORIS.getChildNodeWithName(node, "node-attributes")
        if attrsNode is not None:
            childAttrs = attrsNode.chilNodes
            for attrNode in childAttrs:
                if attrNode.getNodeName() =="label":
                    attrNameNode = PORIS.getChildNodeWithName(attrNode, "name")
                    if (attrNameNode is not None):
                        name = Utils.getTextContent(attrNameNode)
                        attrContentNode = PORIS.getChildNodeWithName(attrNode, "content")
                        if (attrContentNode is not None):
                            visibleNode = PORIS.getChildNodeWithName(attrNode, "visibility")
                            visible = False
                            if (visibleNode is not None):
                                visible =  (Utils.getTextContent(visibleNode) == "true")
                            
                            content = Utils.getTextContent(attrContentNode)
                            attr = PORISAttribute(name,content,visible)
                            self.addAttribute(attr)
                            print("+++++ Hemos añadido a "+self.toString()+" el atributo "+attr)

        destinationsNode = PORIS.getChildNodeWithName(node, "destinations")
        if (destinationsNode is not None):
            childDests = destinationsNode.childNodes
            for destNode in childDests:
                if destNode.getNodeName() == "destination":
                    destId = int(Utils.getTextContent(PORIS.getChildNodeWithName(destNode, "id")))
                    newDest = self._xmlLoaderHashMap[destId]
                    if (newDest is not None):
                        self.addDestination(newDest)

        return ret

    @classmethod
    def fromXML(cls, clase, node: minidom.Node) -> PORIS:
        ret = cls.createInstanceOfClass(clase, "idle")
        if (ret.loadFromXML(node)):
            return ret
        
        else:
            print("Error: It was impossible to create the PORIS from the given XML node")
            return None
    


    @classmethod
    def getInstanceList(cls):
        return cls.__instanceList


    @classmethod
    def getInstance(cls, name:str) -> PORIS:
        for i in cls.__instanceList:
            if i.getName() == name:
                return i
            
        return None

    @classmethod
    def getInstanceForId(cls, id: int) -> PORIS:
        for i in cls.__instanceList:
            if i.getId() == id:
                return i
            
        return None
