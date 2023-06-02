from PORIS import PORIS
from xml.dom import minidom
from ValueFormatter import ValueFormatter
import Utils

class PORISValue(PORIS):
    pass

class PORISValue(PORIS):
    
    def __init__(self, name: str):
        super().__init__(name)
        self.__description = None
        self.__formatter = None

    
    def clone(self, name: str):
        return PORISValue(str)


    def loadFromXML(self, node: minidom.Node) -> bool:
        ret = super().loadFromXML(node)
        instanceFormatterId = int(Utils.getTextContent(PORIS.getChildNodeWithName(node, "value-formatter-id")))
        if (instanceFormatterId is not None):
            self.__formatter = ValueFormatter.getFormatterForId(instanceFormatterId)

        return ret


    def getFormatter(self) -> ValueFormatter:
        return self.__formatter


    def setFormatter(self, formatter: ValueFormatter):
        self.__formatter = formatter
        self.notifyObs()


    def isValid(self, value: PORISValue) -> bool:
        return self.equals(value)


    def getValueForString(self, name: str) -> PORISValue:
        if (self.getName() == name):
            return self
        
        return None


    def getDescription(self)-> str:
        return self.__description


    def setDescription(self, description: str):
        self.__description = description
        self.notifyObs()


    def toString(self) -> str:
        if self.__description is not None:
            return self.__description
        
        return super().toString()


    def toXML(self, doc: minidom.Document, onlyIdent: bool) -> minidom.Element:
        ret = super().toXML(doc, onlyIdent)
        if not onlyIdent:
            if self.getFormatter() is not None:
                formatterIdNode = doc.createElement("value-formatter-id")
                Utils.setTextContent(doc, formatterIdNode, str(self.getFormatter().getId()))
                ret.appendChild(formatterIdNode)

        return ret


    def loadFromXML(self, node: minidom.Node) -> bool:
        ret = super().loadFromXML(node)
        instanceFormatterId = Utils.getTextContent(PORISValue.getChildNodeWithName(node, "value-formatter-id"))
        if (instanceFormatterId is not None):
            self.__formatter = ValueFormatter.getInstanceForId(int(instanceFormatterId))

        return ret
