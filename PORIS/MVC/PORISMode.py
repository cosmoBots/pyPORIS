from PORIS import PORIS
from PORISValue import PORISValue
from PORISNode import PORISNode
from xml.dom import minidom
from ValueFormatter import ValueFormatter
import Utils
from pyPORIS.PORIS.MVC.PORIS import PORIS

class PORISMode(PORIS):
    pass

class PORISMode(PORIS):

    def __init__(self, name: str):
        super().__init__(name)
        self.__defaultValue = None
        self.__defaultSubMode = None


    def addSubMode(self, sm: PORISMode):
        self.addDestination(sm)


    def addValue(self, v: PORISValue):
        self.addDestination(v)


    def getDefaultSubMode(self) -> PORISMode:
        return self.__defaultSubMode
    

    def setDefaultSubMode(self, defaultSubMode: PORISMOde):
        if self.__defaultSubMode != defaultSubMode:
            self.__defaultSubMode = defaultSubMode
            self.notifyObs()

    
    def getDefaultValue(self) -> PORISValue:
        return self.__defaultValue

    
    def setDefaultValue(self, defaultValue: PORISValue):
        if (self.__defaultValue != defaultValue):
            self.__defaultValue = defaultValue
            self.notifyObs()


    def getSubModes(self):
        return self.getFromListByClass(self.__destinations, PORISMode)
    

    def getSuperModes(self):
        return self.getFromListByClass(self.__sources, PORISMode)
    

    def getSystems(self):
        return self.getFromListByClass(self.__sources, PORISNode)

    def getValues(self):
        return self.getFromListByClass(self.__destinations, PORISValue)  


    def getSubModeFromName(self, name: str) -> PORISMode:
        for m in self.getSubModes():
            if m.getName() == name:
                return m
            
    
    def getValueFromName(self, name: str) -> PORISMode:
        for v in self.getValues():
            if v.getName() == name:
                return v
            

    def addDestination(self, child: PORIS):
        if child.isDescendantOf(PORISMode) and self.getDefaultSubMode is not None:
            self.__defaultSubMode = child

        else:
            if (child.isDescendantOf(PORISValue) and self.getDefaultValue() is not None):
                self.__defaultValue = child

        super().addDestination(child)
    


    def toXML(self, doc: minidom.Document, tagClass, onlyIdent: bool) -> minidom.Element:
        ret = super().toXML(doc, tagClass, onlyIdent)
        if (not onlyIdent):
            if self.getDefaultSubMode() is not None:
                defaultSubModeNode = doc.createElement("default-mode-id")
                Utils.setTextContent(doc, defaultSubModeNode, str(self.getDefaultSubMode().getId()))
                ret.appendChild(defaultSubModeNode)

            if self.getDefaultValue() is not None:
                defaultValueNode = doc.createElement("default-value-id")
                Utils.setTextContent(doc, defaultValueNode, str(self.getDefaultValue().getId()))
                ret.appendChild(defaultValueNode)

        return ret