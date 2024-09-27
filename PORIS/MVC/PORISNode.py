from PORIS import PORIS
from PORISMode import PORISMode
from PORISValue import PORISValue
from xml.dom import minidom
from ValueFormatter import ValueFormatter
import Utils

class PORISNode(PORIS):
    pass

class PORISNode(PORIS):

    def __init__(self, name: str):
        super().__init__(name)
        self.__defaultMode = None


    def setDefaultMode(self, defaultMode: PORISMode):
        if (self.__defaultMode != defaultMode):
            self.__defaultMode = defaultMode
            self.notifyObs()


    def getDefaultMode(self) -> PORISMode:
        return self.__defaultMode


    def addMode(self,md):
        self.addDestination(md)


    def addDestination(self, child: PORIS):
        if child.isDescendantOf(PORISMode) and self.getDefaultMode() is None:
            self.__defaultMode = child

        super().addDestination(child)


    def addSubsystem(self, s: PORISNode):
        self.addDestination(s)


    def addValue(self, v: PORISValue):
        self.addDestination(v)

    
    def getModes(self):
        return self.getFromListByClass(self.__destinations, PORISMode)
    

    def getSubsystems(self):
        return self.getFromListByClass(self.__destinations, PORISNode)
    

    def getValues(self):
        return self.getFromListByClass(self.__destinations, PORISValue)
    

    def getModeFromName(self, name:str) -> PORISMode:
        for m in self.getModes():
            if m.getName() == name:
                return m
            
        return None
    

    def getValueFromName(self, name:str) -> PORISValue:
        for v in self.getValues():
            if v.getName() == name:
                return v
            
        return None
    

    def getSubSystemFromName(self,name: str) -> PORISNode:
        for s in self.getSubsystems():
            if s.getName() == name:
                return s
            
        return None
    

    def getDescendantFromName(self, name: str):
        for s in self.getSubsystems():
            if s.getName() == name:
                return s
            
            else:
                ret = s.getDescendantFromName(name)
                if ret != None:
                    return ret
                
        return None

    def xmlTagName(self) -> str:
        return "sub-system"

    def toXML(self, doc: minidom.Document, tagClass, onlyIdent: bool) -> minidom.Element:
        ret = super().toXML(doc, tagClass, onlyIdent)
        if (not onlyIdent):
            if self.getDefaultMode() is not None:
                defaultModeNode = doc.createElement("default-mode-id")
                Utils.setTextContent(doc, defaultModeNode, str(self.getFormatter().getId()))
                ret.appendChild(defaultModeNode)


        return ret
    

    def loadFromXML(self, node: minidom.Node) -> bool:
        ret = super().loadFromXML(node)
        defModId = Utils.getTextContent(PORISValue.getChildNodeWithName(node, "value-formatter-id"))
        if (defModId is not None):
            defMod = PORISMode.getInstanceForId(int(defModId))
            if (defMod is not None):
                self.setDefaultMode(defMod)

        return ret

