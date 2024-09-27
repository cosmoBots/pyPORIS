from PORIS import PORIS
from Model import Model
from Observer import Observer
from xml.dom import minidom
import Utils
import sys

class PORISLib(Model):

    def __init__(self, name: str):
        super().__init__(name)
        self.__nodeList = []


    def clear(self):
        self.__nodeList = []
        self.notifyObs()


    def attach(self, obs: Observer):
        for node in self.__nodeList:
            node.attach(obs)


    def size(self) -> int:
        return len(self.__nodeList)
    

    def last(self) -> PORIS:
        if len(self.__nodeList) > 0:
            return self.__nodeList[-1]
        
        else:
            return None
        

    def addPORISItems(self,items: list):
        for i in items:
            self.__nodeList.append(i)

        self.notifyObs()

    def addPORISItem(self,item: PORIS):
        self.__nodeList.append(item)

        self.notifyObs()

    
    def fromXML(self, node: minidom.Node):
        self.__nodeList = []
        instanceNodes = node.childNodes
        
        for instanceNode in instanceNodes:
            instanceNodeName = instanceNode.getNodeName()
            instanceTypeNode = PORIS.getChildNodeWithName(instanceNode,"type")
            if instanceTypeNode is not None:
                instanceClassName = instanceTypeNode.getTextContent()
                nodeClass = getattr(sys.modules[__name__], instanceClassName)
                if nodeClass is not None:
                    instance = PORIS.fromXML(nodeClass, instanceNode)
                    if instance is not None:
                        self.__nodeList.append(instance)

                    else:
                        print("ERROR!, loading",instanceNodeName,"failed!")

        self.notifyObs()
        return self.__nodeList()
    

    def toXML(self, doc: minidom.Document) -> minidom.Element:
        ret = doc.createElement("poris")
        ret.setAttribute("id","systems")
        ret.setNodeValue("systems")
        for node in self.__nodeList:
            childNode = node.toXML(doc,False)
            if childNode is not None:
                ret.appendChild(childNode)

        return ret







