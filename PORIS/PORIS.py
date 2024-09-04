debug = False

from xml.dom import minidom
from datetime import datetime
from pytz import timezone
import pytz

############################### PORIS subtype classes (not PORIS items) #########################################

############################### PORIS Formatters #########################################

#######################################

class PORISValueFormatter:
    __name = None
    __id = None
    __label = None
    def __init__(self, name: str, id: int, label: str):
        self.__name = name
        self.__id = id
        self.__label = label
        
    def getName(self) -> str:
        return self.__name    
    
    def getId(self) -> int:
        return self.__id    
    
    def getLabel(self) -> str:
        return self.__label

    def toXMLRef(self, dom: minidom.Document) -> minidom.Node:
        n_node = dom.createElement('value-formatter-id')
        n_node.setAttribute("type", "integer")
        if (self.__id != None):
            valueText = dom.createTextNode(str(self.__id))
            n_node.appendChild(valueText)
            
        else:
            n_node.setAttribute("nil", "true")
                  
        return n_node


class PORISValueDateFormatter(PORISValueFormatter):
    #dateFormatString = "dd.MM.yyyy HH:mm:ss z"
    dateFormatString = "%d.%m.%Y %H:%M:%S %z"
    # defaultDateFormatString = "dd.MM.yyyy HH:mm:ss z"
    # oldNoTreatmentFormatString = "yyyy-MM-dd'T'HH:mm:ss'Z'"
    # newNoTreatmentFormatString = "yyyy-MM-dd HH:mm:ss z"
    

    def getValue(self, strValue : str, format: str=dateFormatString) -> datetime:
        return datetime.strptime(strValue, format)
    
    def getString(self, value : datetime, format: str=dateFormatString) -> str:
        return value.strftime(format)
    
    # TODO: Implement the rest of the formatters

######################################    

class PORISValueDoubleFormatter(PORISValueFormatter):
    
    '''
    def getValue(strValue : str, nospecifictreatment: bool=False):
        if nospecifictreatment:
            return super().getValue()
        
        else:
            return float(str)
    
    def getString(value : float, nospecifictreatment: bool=False):
        if nospecifictreatment:
            return super().getString()
        
        else:
            return str(value)
    '''
    def getValue(self, strValue : str, nospecifictreatment: bool=False) -> float:
        return float(strValue)
    
    def getString(self, value : float, nospecifictreatment: bool=False) -> str:
        return str(value)

class PORISValueDMSFormatter(PORISValueDoubleFormatter):

    def getValue(self, strValue : str, nospecifictreatment: bool=False) -> float:
        if nospecifictreatment:
            return super().getValue()
        
        else:
            # TODO: PROCESS IT SPECIFICALLY!!!!
            return float(strValue)
    
    def getString(self, value : float, nospecifictreatment: bool=False) -> str:
        if nospecifictreatment:
            return super().getString()
        
        else:
            # TODO: PROCESS IT SPECIFICALLY!!!!
            return str(value)


class PORISValueHMSFormatter(PORISValueDoubleFormatter):

    def getValue(self, strValue : str, nospecifictreatment: bool=False) -> float:
        if nospecifictreatment:
            return super().getValue()
        
        else:
            # TODO: PROCESS IT SPECIFICALLY!!!!
            return float(strValue)
    
    def getString(self, value : float, nospecifictreatment: bool=False) -> str:
        if nospecifictreatment:
            return super().getString()
        
        else:
            # TODO: PROCESS IT SPECIFICALLY!!!!
            return str(value)

class PORISValueIntegerFormatter(PORISValueDoubleFormatter):

    def getValue(self, strValue : str, nospecifictreatment: bool=False) -> float:
        if nospecifictreatment:
            return super().getValue()
        
        else:
            return int(strValue)
    
    def getString(self, value : float, nospecifictreatment: bool=False) -> str:
        if nospecifictreatment:
            return super().getString(value)
        
        else:
            # TODO: PROCESS IT SPECIFICALLY!!!!
            return str(value)

class PORISValueArcMinFormatter(PORISValueDoubleFormatter):

    pass

class PORISValueArcSecFormatter(PORISValueDoubleFormatter):

    pass

### Create singletons

# <value-formatter-id type="integer" nil="true"/>
PORISVALUEFORMATTER_NIL = PORISValueFormatter("nil",None,None)

# double (null)
# this.formatter = new ValueDoubleFormatter("double", 0);
# <value-formatter-id type="integer" nil="true"></value-formatter-id>
PORISVALUEFORMATTER_DOUBLE = PORISValueFormatter("double",0,None)
 
# public static ValueDoubleFormatter DEFAULT_DOUBLE_FORMATTER = new ValueDoubleFormatter("real", 1, "real");
# <value-formatter-id type="integer">1</value-formatter-id>
PORISVALUEFORMATTER_REAL = PORISValueDoubleFormatter("real",1,"real")

# public static ValueHMSFormatter DEFAULT_HMS_FORMATTER = new ValueHMSFormatter("HH:mm:ss.sss", 2, "HH:mm:ss.sss");
# <value-formatter-id type="integer">2</value-formatter-id>
PORISVALUEFORMATTER_HMS = PORISValueHMSFormatter("HH:mm:ss.sss", 2, "HH:mm:ss.sss")
 
# public static ValueDMSFormatter DEFAULT_DMS_FORMATTER = new ValueDMSFormatter("DD:mm:ss.sss", 3, "DD:mm:ss.sss");
# <value-formatter-id type="integer">3</value-formatter-id>
PORISVALUEFORMATTER_DMS = PORISValueDMSFormatter("DD:mm:ss.sss", 3, "DD:mm:ss.sss")

# public static ValueDoubleFormatter ANGLE_FORMATTER = new ValueDoubleFormatter("angle", 4, "angle");
# <value-formatter-id type="integer">4</value-formatter-id>
PORISVALUEFORMATTER_ANGLE = PORISValueDoubleFormatter("angle", 4, "angle")
 
# public static ValueDoubleFormatter S_FORMATTER = new ValueDoubleFormatter("s", 5, "s");
# <value-formatter-id type="integer">5</value-formatter-id>
PORISVALUEFORMATTER_S = PORISValueDoubleFormatter("s", 5, "s")
 
# public static ValueDateFormatter DEFAULT_DATE_FORMATTER = new ValueDateFormatter("Date", 6, "dd.MM.yyyy HH:mm:ss z");
# <value-formatter-id type="integer">6</value-formatter-id>
PORISVALUEFORMATTER_DATE = PORISValueDateFormatter("Date", 6, "dd.MM.yyyy HH:mm:ss z")

# public static ValueIntegerFormatter DEFAULT_INTEGER_FORMATTER = new ValueIntegerFormatter("integer", 7, "#");
# <value-formatter-id type="integer">7</value-formatter-id>
PORISVALUEFORMATTER_INTEGER = PORISValueIntegerFormatter("integer", 7, "#")
 
# public static ValueArcMinFormatter DEFAULT_ARCMIN_FORMATTER = new ValueArcMinFormatter("arcmin", 8, "arcmin");
# <value-formatter-id type="integer">8</value-formatter-id>
PORISVALUEFORMATTER_ARCMIN = PORISValueArcMinFormatter("arcmin", 8, "arcmin")
 
# public static ValueArcSecFormatter DEFAULT_ARCSEC_FORMATTER = new ValueArcSecFormatter("arcsec", 9, "arcsec");
# <value-formatter-id type="integer">9</value-formatter-id>
PORISVALUEFORMATTER_ARCSEC = PORISValueArcSecFormatter("arcmin", 9, "arcsec")


############################### PORIS item classes #########################################

####################################################
# This class is referenced in advance, to prevent
# circular definition errors

class PORISNode:
    pass


####################################################
# This is the base class for the PORIS items
# contains the common attributes and functions
# subclases overload them when convenient

class PORIS:
    # Public attributes
    id = None               # A numeric id for reference
    ident = None            # A text id for reference
    description = None      # A description of the item
    # Private attributes
    __name = None           # name
    __parent = None         # Parent node (if any)
    __project_id = 0        # The project where the item is described
    __labels = {}           # A list of labels for this item
    
    # Constructor, needs a name for the PORIS item
    def __init__(self,name):
        self.__name = name

    # Name getter
    def getName(self) -> str:
        return self.__name

    # Name setter
    def setName(self, name: str) -> str:
        self.__name = name

    # Parent getter
    def setParent(self, parent: PORISNode):
        self.__parent = parent
    
    # Parent setter
    def getParent(self) -> PORISNode:
        return self.__parent
    
    # Project ID getter
    def getProjectId(self) -> int:
        return self.__project_id

    # Project ID setter
    def setProjectId(self, i: int):
        self.__project_id = i
    
    # Labels list getter   
    def getLabels(self) -> dict:
        return self.__labels

    # Function for adding a label to the labels list    
    def addLabel(self, caption: str, scope_kind: str):
        self.__labels[scope_kind] = caption
        
    def getXMLNodeName(self) -> str:
        return "none"
    
    def getXMLNodeType(self) -> int:
        return 0
    
    def getXMLType(self) -> str:
        return self.__class__.__name__
    
    def toXMLRef(self, dom: minidom.Document) -> minidom.Node:
        idChild = dom.createElement('id')
        idChild.setAttribute("type", "integer")
        valueText = dom.createTextNode(str(self.id))
        idChild.appendChild(valueText)
                  
        return idChild
    
    def getDestinations(self) -> list:
        return []
    
    def toXML(self, dom: minidom.Document) -> minidom.Node:
        n_node = dom.createElement(self.getXMLNodeName())
       
        idChild = dom.createElement('id')
        idChild.setAttribute("type", "integer")
        valueText = dom.createTextNode(str(self.id))
        idChild.appendChild(valueText)
        n_node.appendChild(idChild)
        
        identChild = dom.createElement('ident')
        valueText = dom.createTextNode(self.ident)
        identChild.appendChild(valueText)
        n_node.appendChild(identChild)
                       
        nameChild = dom.createElement('name')
        valueText = dom.createTextNode(self.getName())
        nameChild.appendChild(valueText)
        n_node.appendChild(nameChild)
        
        nodetypeChild = dom.createElement('node-type-id')
        nodetypeChild.setAttribute("type", "integer")
        valueText = dom.createTextNode(str(self.getXMLNodeType()))
        nodetypeChild.appendChild(valueText)
        n_node.appendChild(nodetypeChild)
        
        
        nodetypeChild = dom.createElement('project-id')
        nodetypeChild.setAttribute("type", "integer")
        valueText = dom.createTextNode(str(self.getProjectId()))
        nodetypeChild.appendChild(valueText)
        n_node.appendChild(nodetypeChild)
        
        nodetypeChild = dom.createElement('type')
        valueText = dom.createTextNode(self.getXMLType())
        nodetypeChild.appendChild(valueText)
        n_node.appendChild(nodetypeChild)
        
        destinations_node = dom.createElement('destinations')
        
        dests = self.getDestinations()
        for d in dests:
            destnode = dom.createElement('destination')
            destnode.setAttribute("type", d.getXMLType())
            destnode.appendChild(d.toXMLRef(dom))
            destinations_node.appendChild(destnode)
        
        n_node.appendChild(destinations_node)
        
        nodeAttributesChild = dom.createElement('node-attributes')
        n_node.appendChild(nodeAttributesChild)
        
        '''
        <labels type="array">
            <label>
                <name>Use a pre-imaging file</name>
                <scope-kind>
                    <name>CfgPanel</name>
                </scope-kind>
            </label>
        </labels>
        '''
        
        lbs = self.getLabels()
        

        # For testing only, create a label if there not exist
        if len(lbs) == 0:
            self.addLabel(self.getName(),"test")
            lbs = self.getLabels()

        
        labelsChild = dom.createElement('labels')
        labelsChild.setAttribute("type", "array")
        for l in lbs.keys():
            l_node = dom.createElement("label")
            
            node = dom.createElement("name")
            valueText = dom.createTextNode(lbs[l])
            node.appendChild(valueText)
            l_node.appendChild(node)
            
            node = dom.createElement("scope-kind")
            
            node2 = dom.createElement("name")
            valueText = dom.createTextNode(l)
            node2.appendChild(valueText)
            node.appendChild(node2)       
             
            l_node.appendChild(node)

            labelsChild.appendChild(l_node)
            
        n_node.appendChild(labelsChild)
        
        return n_node

#######################################
        
class PORISValue(PORIS):
    def getXMLNodeName(self) -> str:
        return "value"
    
    def getXMLNodeType(self) -> int:
        return 5
    
    def getXMLFormatter(self) -> PORISValueFormatter:
        return PORISVALUEFORMATTER_NIL

    def toXML(self, dom: minidom.Document) -> minidom.Node:
        n_node = super().toXML(dom)
        n_node.appendChild(self.getXMLFormatter().toXMLRef(dom))
        
        return n_node

    
#######################################

class PORISValueData(PORISValue):
    __data = None
    __default_data = None
    
    def __init__(self,name,default_data):
        super().__init__(name)
        self.__default_data = default_data
        self.__data = default_data

    def getXMLNodeName(self) -> str:
        return "none"

    def setData(self,data):
        self.__data = data
        return self.__data

    def getData(self):
        return self.__data
    
    def getDefaultData(self):
        return self.__default_data
    
    def getXMLNodeName(self) -> str:
        return "sub-system"
    
    def getXMLNodeType(self) -> int:
        return 5

#######################################

class PORISValueString(PORISValueData):
    def __init__(self,name,default_data: str):
        super().__init__(name,default_data)

    def setData(self,data: str):
        return super().setData(data)

    def getData(self) -> str:
        return super().getData()

    def getXMLNodeName(self) -> str:
        return "value-string"


#######################################

class PORISValueFilePath(PORISValueString):

    pass

'''
    <value-file-path>
        <default-string>mypreimagingfile.fits</default-string>
        <id type="integer">628</id>
        <name>PreImagingFile</name>
        <node-type-id type="integer">5</node-type-id>
        <project-id type="integer">17</project-id>
        <type>PORISValueFilePath</type>
        <value-formatter-id type="integer" nil="true"></value-formatter-id>
        <destinations type="array"/>
        <labels type="array"/>
        <file-extension>fits</file-extension>
        <file-description>FITS file</file-description>
        <node-attributes type="array">
            <node-attribute>
                <content>370.0</content>
                <name>rangeMin(&#197;)</name>
                <visibility type="boolean">true</visibility>
            </node-attribute>  
        </node-attributes>
    </value-file-path>
'''

class PORISValueDate(PORISValueString):

    def getXMLFormatter(self) -> PORISValueFormatter:
        return PORISVALUEFORMATTER_DATE



'''

    public static ValueDateFormatter DEFAULT_DATE_FORMATTER = new ValueDateFormatter("Date", 6, "dd.MM.yyyy HH:mm:ss z");
    <value-formatter-id type="integer">6</value-formatter-id>


    <value-date-range>
        <date-max type="timestamp">2016-12-31 23:59:00 UTC</date-max>
        <date-min type="timestamp">2006-02-01 00:00:00 UTC</date-min>
        <default-date type="timestamp">2011-04-09 00:00:00 UTC</default-date>
        <id type="integer">613</id>
        <name>Date</name>
        <node-type-id type="integer">5</node-type-id>
        <project-id type="integer">17</project-id>
        <type>PORISValueDate</type>
        <value-formatter-id type="integer">6</value-formatter-id>
        <destinations type="array"/>
        <labels type="array"/>
        <node-attributes type="array"/>
    </value-date-range>
'''

#######################################

class PORISValueFloat(PORISValueData):
    __min = None
    __max = None

    def __init__(self,name: str,min: float,default_data: float, max:float):
        super().__init__(name,default_data)
        self.__min = min
        self.__max = max

    def setData(self,data :float) -> float:
        if debug:
            print("Applying", data, "name:", self.getName(), "min:", self.__min, "max:", self.__max)

        if data >= self.__min:
            if data <= self.__max:
                return super().setData(data)
                
        return self.getData()

    def getData(self) -> float:
        return super().getData()
    
    def getMin(self) -> float:
        return self.__min

    def getMax(self) -> float:
        return self.__max

    def getXMLNodeName(self) -> str:
        return "value-double-range"
    
    def getXMLFormatter(self) -> PORISValueFormatter:
        return PORISVALUEFORMATTER_REAL

    def toXML(self, dom: minidom.Document) -> minidom.Node:
        '''
        <default-float type="float">200</default-float>
        <rangemax type="float">1000</rangemax>
        <rangemin type="float">0</rangemin>    
        '''
        n_node = super().toXML(dom)
        defaultfloatnode = dom.createElement("default-float")
        defaultfloatnode.setAttribute("type","float")
        valueText = dom.createTextNode(str(self.getDefaultData()))
        defaultfloatnode.appendChild(valueText)
        n_node.appendChild(defaultfloatnode)
        rangemaxnode = dom.createElement("rangemax")
        rangemaxnode.setAttribute("type","float")
        valueText = dom.createTextNode(str(self.getMax()))
        rangemaxnode.appendChild(valueText)
        n_node.appendChild(rangemaxnode)
        rangeminnode = dom.createElement("rangemin")
        rangeminnode.setAttribute("type","float")
        valueText = dom.createTextNode(str(self.getMin()))
        rangeminnode.appendChild(valueText)
        n_node.appendChild(rangeminnode)
        
        return n_node

#######################################

class PORISMode(PORIS):
    
    def __init__(self,name):
        super(PORISMode, self).__init__(name)
        self.values = {}
        self.submodes = {}
        
    def addSubMode(self,m):
        self.submodes[m.id] = m

    def addValue(self,v):
        self.values[v.id] = v
    
    def getEligibleValue(self,v,current) -> PORISValue:
        if debug:
            if (v != None):
                print("Entro en PORISMode getEligibleValue para el modo", self.getName(), "con valor propuesto", v.getName())
            else:
                print("Entro en PORISMode getEligibleValue para el modo", self.getName(), "con valor propuesto NULO")
    
            print("Valores posibles para este modo",self.values.keys())

        ret = None
        if v.id in self.values.keys():
            ret = v
        else:
            if current.id in self.values.keys():
                ret = current
            else:
                itk = list(self.values.keys())[0]
                ret = self.values[itk]

        # print("ret queda",ret.getName())
        return ret
    
    def getEligibleSubMode(self,m,current):
        if debug:
            print("Entro en PORISMode getEligibleSubMode para el modo", self.getName(), "con m =", m.getName())

        ret = None
        found = False

        if debug:
            print("Submodos:",self.submodes.keys())

        if m.id in self.submodes.keys():
            ret = m
        
        else:
            if current.id in self.submodes.keys():
                ret = current
                
            else:
                # If none of two are found, search the first submode with the same parent
                if debug:
                    print("None of the two given, I have only these keys",self.submodes.keys())

                for ks in self.submodes.keys():
                    s = self.submodes[ks]
                    if debug:
                        print(s.getParent(),s.getParent().getName())

                    if s.getParent() == m.getParent():
                        ret = s
                        break
                
                if ret is None:
                    # None of the given or applicable, I have to apply the first (UNKNOWN mode)
                    ret = m.getParent().modes[list(m.getParent().modes.keys())[0]]
                

        return ret
    
    def getEligibleValueFromIdx(self,idx,current):
        vk = list(self.values.keys())[idx]
        result = self.getEligibleValue(self.values[vk],current)
        if result is None:
            ret = 0
        else:
            ret = result.idx
        
        return ret
    
    def getEligibleSubModeFromIdx(self,idx,current):
        mk = list(self.submodes.keys())[idx]
        result = self.getEligibleSubMode(self.submodes[mk],current)
        if result is None:
            ret = 0
        else:
            ret = result.idx
        
        return ret
    
    def getDestinations(self) -> list:
        ret = []
        for k in self.values:
            ret.append(self.values[k])

        for k in self.submodes:
            ret.append(self.submodes[k])
            
        return ret
    
    def getXMLNodeName(self) -> str:
        return "mode"
    
    def getXMLNodeType(self) -> int:
        return 6
    
    def toXML(self, dom: minidom.Document) -> minidom.Node:
        '''
        <default-mode-id type="integer" nil="true"/>
        <default-value-id type="integer" nil="true"/>
        '''            
        n_node = super().toXML(dom)
        defaultmodenode = dom.createElement("default-mode-id")
        defaultmodenode.setAttribute("type","integer")
        defaultmodenode.setAttribute("nil","true")
        n_node.appendChild(defaultmodenode)
        defaultvaluenode = dom.createElement("default-value-id")
        defaultvaluenode.setAttribute("type","integer")
        defaultvaluenode.setAttribute("nil","true")
        n_node.appendChild(defaultvaluenode)
        
        return n_node

    
    
#######################################    
    
class PORISNode(PORIS):
    __selectedMode = None

    def __init__(self,name):
        super(PORISNode, self).__init__(name)
        self.modes = {}
    
    
    def addMode(self,m):
        self.modes[m.id] = m
        m.setParent(self)
        if self.__selectedMode == None:
            self.__selectedMode = m

    def init(self):
        if debug:
            print("Init de",self.getName(),", número de modos:" , len(self.modes))

        firstMode = self.modes[list(self.modes.keys())[0]]
        if debug:
            print("Init ", self.getName() + ":",firstMode.getName())

        self.__selectedMode = firstMode
    
    def setEligibleMode(self):
        if debug:
            print("Entro en PORISNode setEligibleMode", self.getName())

        if self.getSelectedMode() is None:
            if debug:
                print("- selectedMode es NULO")

            self.init()
            
        if debug:
            print("- selectedMode es ahora", self.getSelectedMode().getName())

        # TODO: Check if this selectMode is redundant
        return self.selectMode(self.getSelectedMode())

    def selectMode(self,m):
        self.__selectedMode = m
        return m

    def setModeFromIdx(self,idx):
        mk = list(self.modes.keys())[idx]
        result = self.selectMode(self.modes[mk])
        if result is None:
            ret = 0
        else:
            ret = result.idx
        
        if debug:
            print("Acaba la operación selectMode con resultado", ret)

        return ret

    def getEligibleMode(self,m):
        if debug:
            print("Entro en PORISNode ",self.getName(), ".getEligibleMode("+m.getName()+")")

        ret = None
        if self.getParent() is None:
            if debug:
                print("El padre de", self.getName(), "es nulo")

            ret = m
        
        else:
            if debug:
                print("Buscamos entre los", len(self.getParent().getSelectedMode().submodes),"submodos de",self.getParent().getName())
                print("selectedMode",self.getSelectedMode().getName(),m.getName())

            ret = self.getParent().getSelectedMode().getEligibleSubMode(m,self.getSelectedMode())

        if ret is None:
            if debug:
                print("No hubo suerte, el modo a seleccionar es nulo")
        
        else:
            if debug:
                print("El modo seleccionado es",ret.getName())
        
        return ret


    def getEligibleModeFromIdx(self,idx):
        mk = list(self.modes.keys())[idx]
        result = self.getEligibleMode(self.submodes[mk])
        if result is None:
            ret = 0
        else:
            ret = result.idx
        
        return ret

    def getModeFromId(self,myid):
        ret = None
        if myid in self.modes.keys():
            ret = self.modes[myid]

        return ret        

    def getModeFromName(self,myname):
        ret = None
        for myid in self.modes.keys():
            if self.modes[myid].getName() == myname:
                ret = self.modes[myid]

        return ret

    def getSelectedMode(self) -> PORISMode:
        return self.__selectedMode

    def getDestinations(self) -> list:
        ret = []
        for k in self.modes:
            ret.append(self.modes[k])
            
        return ret

    def getXMLNodeName(self) -> str:
        return "sub-system"
    
    def getXMLNodeType(self) -> int:
        return 4
    
    def toXML(self, dom: minidom.Document) -> minidom.Node:
        '''
        <default-mode-id type="integer" nil="true"/>
        <default-value-id type="integer" nil="true"/>
        '''            
        n_node = super().toXML(dom)
        defaultmodenode = dom.createElement("default-mode-id")
        defaultmodenode.setAttribute("type","integer")
        defaultmodenode.setAttribute("nil","true")
        n_node.appendChild(defaultmodenode)
        
        return n_node    

#######################################

class PORISParam(PORISNode):
    __selectedValue = None
  
    def __init__(self,name):
        super(PORISParam, self).__init__(name)
        self.values = {}
  
    def getSelectedValue(self):
        return self.__selectedValue
    
    def addValue(self,v):
        self.values[v.id] = v
        v.setParent(self)
        if self.__selectedValue == None:
            self.__selectedValue = v

    def setEligibleValue(self):
        if debug:
            print("Entro en PORISParam setEligibleValue", self.getName())

        return self.setValue(self.__selectedValue)
    
    def selectMode(self,m):
        if debug:
            print("Entro en Param",self.getName()+".selectMode("+ m.getName()+"\")")

        ret = self.getEligibleMode(m)

        if debug:
            print("Estoy en",self.getName())
            print(list(self.modes.keys()))

        if ret is None:
            mk = list(self.modes.keys())[0]
            ret = self.modes[mk]

        if ret != self.getSelectedMode():
            super(PORISParam,self).selectMode(ret)
            self.setValue(self.__selectedValue)

        return ret

    def getValueFromId(self,myid):
        ret = None
        if myid in self.values.keys():
            ret = self.values[myid]

        return ret

    def getValueFromName(self,myname):
        ret = None
        for myid in self.values.keys():
            if self.values[myid].getName() == myname:
                ret = self.values[myid]

        return ret


    def getEligibleValue(self,v,current):
        if debug:
            if v is None:
                print("Entro en PORISParam getEligibleValue ", self.getName(), "con valor NULO")
            else:
                print("Entro en PORISParam getEligibleValue ", self.getName(), "con valor", v.getName())

            print("***",self.getName(),self.getSelectedMode().getName(),self.modes)

        ret = None
        
        if self.getSelectedMode() is None:
            if debug:
                print("- selectedMode es NULO")

            self.init()

        ret = self.getSelectedMode().getEligibleValue(v,current)
        
        return ret

    def setValue(self,v):
        if debug:
            if v is None:
                print("Entro en PORISParam setValue", self.getName(), "con valor NULO")
            else:
                print("Entro en PORISParam setValue", self.getName(), "con valor", v.getName())

        ret = self.getEligibleValue(v,self.__selectedValue)
        if ret != self.__selectedValue:
            # First, try to copy the existing data
            # print("Vamos a aplicar el valor" , ret.getName())
            if isinstance(self.__selectedValue,PORISValueData.__class__):
                print(ret.getName(),"es un PORISValueData")
                print(ret.__class__.__name__)
                v = self.__selectedValue
                print(v.getName())
                print(ret.getName())
                data = v.getData()
                ret.setData(data)

            # Then select the new value
            self.__selectedValue = ret
            
        return ret

    def getEligibleValueFromIdx(self,idx,current):
        vk = list(self.values.keys())[idx]
        result = self.getEligibleValue(self.values[vk],current)
        if result is None:
            ret = 0
        else:
            ret = result.idx
        
        return ret

    def setValueFromIdx(self,idx):
        vk = list(self.values.keys())[idx]
        result = self.setValue(self.values[vk])
        if result is None:
            ret = 0
        else:
            ret = result.idx
        
        return ret
    
    def getDestinations(self) -> list:
        ret = super().getDestinations()
        for k in self.values:
            ret.append(self.values[k])
            
        return ret
    
    
    def getXMLType(self) -> str:
        return "PORISNode"


#######################################

class PORISSys(PORISNode):

    def __init__(self,name):
        super(PORISSys, self).__init__(name)
        self.params = {}
        self.subsystems = {}

    def addParam(self,p):
        self.params[p.id] = p
        p.setParent(self)

    def addSubsystem(self,s):
        self.subsystems[s.id] = s
        s.setParent(self)
        
    def selectMode(self,m):
        if debug:
            print("Entro en Sys selectMode de", self.getName(), "con modo", m.getName())

        ret = self.getEligibleMode(m)
        if ret is None:
            if debug:
                print("el nuevo modo es NULO que es diferente del seleccionado")
                print(" Hemos de poner el modo UNKNOWN, que por defecto es el primero")

            mk = list(self.modes.keys())[0]
            ret = self.modes[mk]

        if ret != self.getSelectedMode():
            if debug:
                print("el nuevo modo es", ret.getName())
                if self.getSelectedMode() is not None:
                    print (" que es diferente de",self.getSelectedMode().getName())
                else:
                    print(" que es diferente de NULO")

            super(PORISSys, self).selectMode(ret)
            
            for k in self.params.keys():
                p = self.params[k]
                p.setEligibleMode()

            for k in self.subsystems.keys():
                s = self.subsystems[k]
                s.setEligibleMode()
   
        else:
            if debug:
                print("el modo escogido es el mismo", ret.getName())

        if debug:
            print("Salgo de Sys selectMode de", self.getName(), "con m="+m.getName(), "y resultado =",ret.getName())

        return ret

    def setEligibleMode(self):
        if debug:
            print("Entro en PORISSys setEligibleMode", self.getName())

        if self.getSelectedMode() is None:
            if debug:
                print("- selectedMode es NULO")

            self.init()
            
        if debug:
            print("- selectedMode es ahora", self.getSelectedMode().getName())

        # TODO: Check if this selectMode is redundant
        return self.selectMode(self.getSelectedMode())
    
    def getSubSystemFromId(self,myid):
        ret = None
        if myid in self.subsystems.keys():
            ret = self.subsystems[myid]

        return ret
    
    def getSubParamFromId(self,myid):
        ret = None
        if myid in self.params.keys():
            ret = self.params[myid]

        return ret
    
    def getSubParamFromName(self,myname):
        ret = None
        for myid in self.params.keys():
            if (self.params[myid].getName() == myname):
                ret = self.params[myid]

        return ret
        
    def getDescendantFromId(self,myid):
        ret = self.getSubSystemFromId(myid)
        if ret is None:
            for sk in self.subsystems.keys():
                s = self.subsystems[sk]
                ret = s.getDescendantFromId(myid)
                if ret is not None:
                    break

        return ret
    
    def getDescendantParamFromId(self,myid):
        ret = self.getSubParamFromId(myid)
        if ret is None:
            print("no es un hijo directo")
            print(myid,self.myid,self.subsystems)
            for sk in self.subsystems.keys():
                if debug:
                    print(sk)

                s = self.subsystems[sk]
                ret = s.getDescendantParamFromID(myid)
                if ret is not None:
                    if debug:
                        print("Tenemos",ret)

                    break

        return ret

    def getDescendantParamFromName(self,myname):
        ret = self.getSubParamFromName(myname)
        if ret is None:
            print("no es un hijo directo")
            print(myname,self.id,self.subsystems)
            for sk in self.subsystems.keys():
                if debug:
                    print(sk)

                s = self.subsystems[sk]
                ret = s.getDescendantParamFromName(myname)
                if ret is not None:
                    if debug:
                        print("Tenemos",ret)

                    break

        return ret

    def getDestinations(self) -> list:
        ret = super().getDestinations()
        for k in self.subsystems:
            ret.append(self.subsystems[k])
        
        for k in self.params:
            ret.append(self.params[k])
                    
        return ret

    def getXMLType(self) -> str:
        return "PORISNode"


#######################################

class PORISDoc:
    __id_counter = 1
    __node_dict = {}
    __root = None
    __project_id = 0
    
    def __init__(self,project_id):
        self.__project_id = project_id
        print("Setting the project_id to ", self.__project_id)
        
    def setProjectId(self, i: int):
        self.__project_id = i
        
    def getProjectId(self) -> int:
        return self.__project_id
    
    def setRoot(self, r:PORIS):
        self.__root = r
        print("Setting the root to ", r.getName(),"and",self.__root.getName(),"and",self.getName())
        
    def getRoot(self) -> PORIS:
        return self.__root        
        
    def getName(self):
        return self.__root.getName()
        
    def addNode(self, n: PORIS):
        n.id = self.__id_counter
        self.__node_dict[str(n.id)] = n
        n.setProjectId(self.__project_id)
        self.__id_counter += 1

    def list_nodes(self):
        print(len(self.__node_dict))
        for k in self.__node_dict.keys():
            n = self.__node_dict[k]
            print(str(n.id),n.getName())
        
    # Gets a list of PORIS items IDs sorted so their items
    # are never referencing in their destinations a node which has not been 
    # listed before.  This is very convenient, because some consumers of products created
    # from the list - like the PorisGUI panels, which will load the XML created with toXML() -  
    # may have issues if they process items referencing other items which have not been processed before.
    def getConsistentReferencesSortedIdsList(self) -> list:
        node_and_destinations = {}
        for k in self.__node_dict.keys():
            # print(k)
            n = self.__node_dict[k]
            thisnode = {}
            thiskey = k
            destinations = []
            for d in n.getDestinations():
                destinations.append(str(d.id))
                
            node_and_destinations[thiskey] = destinations


        # print(node_and_destinations)
        # print("----> Initial LEN ", len(node_and_destinations))
        # print("################################")
        
        finished = False
        ordered_list = []
        
        while not finished:
            # Let's look for nodes without destinations
            nodes_without_destinations = []
            for k in node_and_destinations:
                # print(k, len(node_and_destinations[k]), node_and_destinations[k])
                if len(node_and_destinations[k]) == 0:
                    nodes_without_destinations.append(int(k))

            # Now, let's add them to the ordered list
            ordered_list += nodes_without_destinations

            # print("################################")
            # print("----> To remove ", len(nodes_without_destinations))
            # print(nodes_without_destinations)

                    
            # And let's remove them from the nodes_and_destinations dictionary
            for id in nodes_without_destinations:
                del node_and_destinations[str(id)]

            # print(node_and_destinations)
            # print("----> LEN ", len(node_and_destinations))

            # And now let's remove their references from node_and_destinations list
            for k in node_and_destinations:
                toremove = []
                for d in node_and_destinations[k]:
                    # print(k, node_and_destinations[k])
                    # print("Trying to remove",d,"from",node_and_destinations[k])
                    # print("The list of nodes without destinations is ", nodes_without_destinations)
                    if int(d) in nodes_without_destinations:
                        # print("Removing",d,"from",k,node_and_destinations[k])
                        toremove.append(d)
                        # print("Remaining",node_and_destinations[k])
            
                for d in toremove:
                    node_and_destinations[k].remove(d)

            # print("----> Final LEN ", len(node_and_destinations))
            
            finished = len(node_and_destinations) == 0

            
        # print(len(ordered_list),ordered_list)
        return ordered_list
        
                    
    def toXML(self) -> minidom.Document:
        rootInstr = minidom.Document()
        xmlInstr = rootInstr.createElement('poris')
        rootInstr.appendChild(xmlInstr)

        # In order to prevent void references in the consumer, we have to use an ordered list of nodes
        # with no back-references
        ordered_list = self.getConsistentReferencesSortedIdsList()
        for id in ordered_list:
            n = self.__node_dict[str(id)]
            n_node = n.toXML(rootInstr)
            if (n_node == None):
                print("ERROR: ",n.getName())
                
            else:
                xmlInstr.appendChild(n_node)
            
        return rootInstr
        