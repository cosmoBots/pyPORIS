debug = False

from xml.dom import minidom
from datetime import datetime
from pytz import timezone
import pytz

############################### PORIS subtype classes (not PORIS items) #########################################

############################### PORIS Formatters #########################################

#######################################

class PORISValueFormatter:
    pass

class PORISValueFormatter:

    instances = {}
    def __init__(self, name: str, id: int, label: str):
        self.__name = name
        self.__id = id
        self.__label = label
        PORISValueFormatter.instances[str(id)] = self
        
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

    # Recovers the id of the item from a reference
    def fromXMLRef(n_node: minidom.Node) -> PORISValueFormatter:
        idnode = n_node.getElementsByTagName('value-formatter-id')[0]
        for t in idnode.childNodes:
            if t.nodeType == t.TEXT_NODE:
                return PORISValueFormatter.instances[t.nodeValue]
            
        return None

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


############################### PORIS item classes ############################################################

####################################################
# This class is referenced in advance, to prevent
# circular definition errors

class PORISNode:
    pass

class PORISDoc:
    pass


####################################################
# This is the base class for the PORIS items
# contains the common attributes and functions
# subclases overload them when convenient
class PORIS:
    pass
class PORIS:
    # Constructor, needs a name for the PORIS item
    def __init__(self,name):
        # Public attributes
        self.id = None               # A numeric id for reference
        self.ident = None            # A text id for reference
        self.description = None      # A description of the item
        self.document = None
        # Private attributes
        self.__name = name           # name
        self.__parent = None         # Parent node (if any)
        self.__labels = {}           # A dictionary of labels for this item, the scope_kind acts as a key
        self.__node_attributes = {}  # A dictionary of node attributes for this item, the content acts as a key
        self.__project_id = 0 # The project where the item is described

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

    # Function for adding a label to the labels list.
    # caption is the string to show within a context
    # scope_kind is an identifier of the context where the caption applies
    def setLabel(self, caption: str, scope_kind: str):
        self.__labels[scope_kind] = caption
    
    # Labels list getter   
    def getNodeAttributes(self) -> dict:
        return self.__node_attributes

    # Function for setting a node attribute to the node attributes list.
    # name is the string to show as the caption and identifier of the attribute
    # it can also include units
    # content is the value of the attribute
    # visibility is a flag which determines if the attribute shall be shown to end users, or kept hidden for them
    def setNodeAttribute(self, name: str, content: str, visibility: bool):
        self.__node_attributes[name] = {"content": content, "visibility": visibility }
   
    # Getter for the destinations of this item
    # It will be overloaded by subclasses
    def getDestinations(self) -> list:
        return []
       
    ########## XML related functions ########
    
    # Getter for the node name (tag name) which depends of the class.
    # It will be overloaded by subclasses
    def getXMLNodeName(self) -> str:
        return "none"
    
    # Getter for the nodetype which depends of the class.
    # It will be overloaded by subclasses
    def getXMLNodeType(self) -> int:
        return 0
    
    # Getter for the type which depends of the class, by default is the class name
    # It can overloaded by subclasses.
    def getXMLType(self) -> str:
        return self.__class__.__name__
    
    # Builds a reference for the item, to be used mainly inside the "destination" tag
    def toXMLRef(self, dom: minidom.Document) -> minidom.Node:
        ret = dom.createElement('id')
        ret.setAttribute("type", "integer")
        valueText = dom.createTextNode(str(self.id))
        ret.appendChild(valueText)
        return ret
    
    # Recovers the id of the item from a reference
    def fromXMLRef(n_node: minidom.Node, pdoc: PORISDoc) -> PORIS:
        idnode = n_node.getElementsByTagName('id')[0]
        if idnode.nodeType == idnode.TEXT_NODE:
            return pdoc.getItem(int(idnode.nodeValue))
            
        return None

    # Dumps the current item to an XML node
    # PORIS items, after calling this function using super().toXML(doc), 
    # will add additional nodes which will depend on the class
    def toXML(self, dom: minidom.Document) -> minidom.Node:
        # Tag name will be normally the class name, but it can be overloaded
        # so we use a function to get it
        n_node = dom.createElement(self.getXMLNodeName())
       
        # subnode with the name of the item
        nameChild = dom.createElement('name')
        valueText = dom.createTextNode(self.getName())
        nameChild.appendChild(valueText)
        n_node.appendChild(nameChild)
       
        # subnode with an identifying integer
        idChild = dom.createElement('id')
        idChild.setAttribute("type", "integer")
        valueText = dom.createTextNode(str(self.id))
        idChild.appendChild(valueText)
        n_node.appendChild(idChild)
        
        # subnode with the type
        nodetypeChild = dom.createElement('type')
        valueText = dom.createTextNode(self.getXMLType())
        nodetypeChild.appendChild(valueText)
        n_node.appendChild(nodetypeChild)
        
        # subnode with the node type id
        nodetypeChild = dom.createElement('node-type-id')
        nodetypeChild.setAttribute("type", "integer")
        valueText = dom.createTextNode(str(self.getXMLNodeType()))
        nodetypeChild.appendChild(valueText)
        n_node.appendChild(nodetypeChild)
        
        # ubnode with an identifying string
        identChild = dom.createElement('ident')
        valueText = dom.createTextNode(self.ident)
        identChild.appendChild(valueText)
        n_node.appendChild(identChild)
                               
        # subnode with the project id
        nodetypeChild = dom.createElement('project-id')
        nodetypeChild.setAttribute("type", "integer")
        valueText = dom.createTextNode(str(self.getProjectId()))
        nodetypeChild.appendChild(valueText)
        n_node.appendChild(nodetypeChild)

        # array of labels       
        lbs = self.getLabels()
        '''
        # For testing only, create a label if there not exist
        if len(lbs) == 0:
            self.setLabel(self.getName(),"test")
            lbs = self.getLabels()

        '''
        labelsChild = dom.createElement('labels')
        labelsChild.setAttribute("type", "array")
        for l in lbs.keys():
            # Each label is an entry in the labels dict
            # The value is the caption, which shall
            # be published under the "name" tag
            l_node = dom.createElement("label") 
            namenode = dom.createElement("name")
            valueText = dom.createTextNode(lbs[l])
            namenode.appendChild(valueText)
            l_node.appendChild(namenode)
            # The scope_kind is the key, which shall
            # be published under the scope-kind tag
            scopenode = dom.createElement("scope-kind")
            
            sknamenode = dom.createElement("name")
            valueText = dom.createTextNode(l)
            sknamenode.appendChild(valueText)
            scopenode.appendChild(sknamenode)       
             
            l_node.appendChild(scopenode)

            labelsChild.appendChild(l_node)
            
        n_node.appendChild(labelsChild)
        
        # array of destinations, containing their XML references
        destinations_node = dom.createElement('destinations')
        destinations_node.setAttribute("type","array")
        dests = self.getDestinations()
        for d in dests:
            destnode = dom.createElement('destination')
            destnode.setAttribute("type", d.getXMLType())
            destnode.appendChild(d.toXMLRef(dom))
            destinations_node.appendChild(destnode)
        
        n_node.appendChild(destinations_node)
        
        # array of node attributes

        nats = self.getNodeAttributes()

        nodeAttributesChild = dom.createElement('node-attributes')
        nodeAttributesChild.setAttribute("type", "array")
        '''
            <node-attribute>
                <content>370.0</content>
                <name>rangeMin(&#197;)</name>
                <visibility type="boolean">true</visibility>
            </node-attribute>  
        '''
        for l in nats.keys():
            # Each label is an entry in the labels dict
            # The value is the caption, which shall
            # be published under the "name" tag
            nat_node = dom.createElement("node-attribute") 

            contentnode = dom.createElement("content")
            valueText = dom.createTextNode(nats[l]["content"])
            contentnode.appendChild(valueText)
            nat_node.appendChild(contentnode)

            namenode = dom.createElement("name")
            valueText = dom.createTextNode(l)
            namenode.appendChild(valueText)
            nat_node.appendChild(namenode)

            visnode = dom.createElement("visibility")
            visnode.setAttribute("type","boolean")
            if (nats[l]["visibility"]):
                valueText = dom.createTextNode("true")

            else:
                valueText = dom.createTextNode("false")

            visnode.appendChild(valueText)
            nat_node.appendChild(visnode)

            nodeAttributesChild.appendChild(nat_node)
            
        n_node.appendChild(nodeAttributesChild)    
        
        # PORIS items, after calling this function using super().toXML(doc), 
        # will add additional nodes which will depend on the class
        
        return n_node

    # Creates the object instance from an XML node
    def fromXML(n_node: minidom.Node, pdoc: PORISDoc) -> PORIS:
        name = None
        ident = None
        for e in n_node.childNodes:
            if e.localName == "name":
                for c in e.childNodes:
                    if c.nodeType == c.TEXT_NODE:
                        name = c.nodeValue
                        break

            if e.localName == "id":
                for c in e.childNodes:
                    if c.nodeType == c.TEXT_NODE:
                        id = int(c.nodeValue)
                        break

            if e.localName == "type":
                for c in e.childNodes:
                    if c.nodeType == c.TEXT_NODE:
                        break

            if e.localName == "ident":
                for c in e.childNodes:
                    if c.nodeType == c.TEXT_NODE:
                        ident = c.nodeValue
                        break

        ret = PORIS(name)
        ret.ident = ident
        pdoc.addItem(ret, id)
        
        return ret

##################################################
# Base class for all the PORISValue items
# Values may have a formatter associated to it
# if no subclassed, then the item will not take any data
# Users just select the PORISValue and it's done

class PORISValue(PORIS):
    pass

class PORISValue(PORIS):
    
    def __init__(self,name):
        super().__init__(name)
        self.__formatter = PORISVALUEFORMATTER_NIL

    ########## XML related functions ########
        
    # the tag name will be "value", but subclasses
    # might overload it
    def getXMLNodeName(self) -> str:
        return "poris-value"
    
    # getter for the node type (overloading PORIS one)
    def getXMLNodeType(self) -> int:
        return 5
    
    def getXMLFormatter(self) -> PORISValueFormatter:
        return self.__formatter
    
    def setXMLFormatter(self, formatter: PORISValueFormatter):
        self.__formatter = PORISVALUEFORMATTER_NIL

    # Dumps the item's XML (uses PORIS superclass' one and appends information of the formatter)
    def toXML(self, dom: minidom.Document) -> minidom.Node:
        n_node = super().toXML(dom)
        n_node.appendChild(self.getXMLFormatter().toXMLRef(dom))
        
        return n_node

    # Creates the object instance from an XML node
    def fromXML(n_node: minidom.Node, pdoc: PORISDoc) -> PORISValue:
        ret = super(PORISValue,PORISValue).fromXML(n_node, pdoc)
        ret.__class__ = PORISValue
        formatter = PORISValueFormatter.fromXMLRef(n_node)
        ret.setXMLFormatter(formatter)
        
        return ret

    
########################################################
# Base class for the PORISValue items which contain data
# Apart for selecting the PORISValue, user has also to define the data
# data examples are strings, integers, floats, dates, angles, etc.

class PORISValueData(PORISValue):
    pass

class PORISValueData(PORISValue):
    
    # Constructor, appends data and default data
    # initializers to the super() constructor
    def __init__(self,name,default_data):
        super().__init__(name)
        # The current data will be the default one at the beginning
        self.__default_data = default_data
        self.__data = default_data

    # Data getter
    def getData(self):
        return self.__data
    
    # Data setter
    def setData(self,data):
        self.__data = data
        return self.__data

    # Default data getter
    def getDefaultData(self):
        return self.__default_data
    
    def setDefaultData(self, d):
        self.__default_data = d
    
    ########## XML related functions ########
    
    # The tag is "none" because this class shall never
    # be instanced directly
    def getXMLNodeName(self) -> str:
        return "none"

    # The node type is 0 because this class shall never
    # be instanced directly
    def getXMLNodeType(self) -> int:
        return 0

    # Creates the object instance from an XML node
    def fromXML(n_node: minidom.Node, pdoc: PORISDoc) -> PORISValueData:
        ret = super(PORISValueData,PORISValueData).fromXML(n_node, pdoc)
        ret.__class__ = PORISValueData
        formatter = PORISValueFormatter.fromXMLRef(n_node)
        ret.setXMLFormatter(formatter)
        
        return ret

#######################################

class PORISValueString(PORISValueData):
    
    def __init__(self,name,default_data: str):
        super().__init__(name,default_data)

    # Getter for the data, it is overloading
    # superclass one, but adding control over datatype
    def getData(self) -> str:
        return super().getData()

    # Setter for the data, it is overloading
    # superclass one, but adding control over datatype
    def setData(self,data: str) -> str:
        return super().setData(data)

    ########## XML related functions ########

    # getter for the XML tag name
    def getXMLNodeName(self) -> str:
        return "poris-value-string"

    # The node type is 6 for PORISValueStrings
    def getXMLNodeType(self) -> int:
        return 6


#######################################
# This class is a PORISValuestring for storing a filepath
# TODO: Develop this class
class PORISValueFilePath(PORISValueString):

    ########## XML related functions ########
    
    # Getter for the XML tag name of this item
    def getXMLNodeName(self) -> str:
        return "poris-value-file-path"

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

#######################################
# This class stores Dates in a PORISValueString
# The difference is in the formatter, and 
# in the XML 
# TODO: Develop this class
class PORISValueDate(PORISValueString):

    ########## XML related functions ########
    
    # Getter for the XML tag name of this item
    def getXMLNodeName(self) -> str:
        return "poris-value-date"    
    # getter for the XML tag name
    def getXMLFormatter(self) -> PORISValueFormatter:
        return PORISVALUEFORMATTER_DATE

'''
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
# This class allows Flat data in a PORISValue
class PORISValueFloat(PORISValueData):
    pass
class PORISValueFloat(PORISValueData):

    # Constructor, overloads PORISValueData and ads min and max values
    def __init__(self,name: str,min: float,default_data: float, max:float):
        super().__init__(name,default_data)
        self.__min = min
        self.__max = max

    # Data getter, uses super()'s, but restricts data type
    def getData(self) -> float:
        return super().getData()

    # Data setter, checks range limits and restricts data type
    def setData(self,data :float) -> float:
        if debug:
            print("Applying", data, "name:", self.getName(), "min:", self.__min, "max:", self.__max)

        if data >= self.__min:
            if data <= self.__max:
                return super().setData(data)
                
        return self.getData()
    
    # min getter
    def getMin(self) -> float:
        return self.__min

    # max getter
    def getMax(self) -> float:
        return self.__max

    ########## XML related functions ########
    
    # getter for the XML tag name
    def getXMLNodeName(self) -> str:
        return "poris-value-float"
    
    # getter for the formatter, overload super()'s
    def getXMLFormatter(self) -> PORISValueFormatter:
        return PORISVALUEFORMATTER_REAL

    # Dumps item to XML, uses super().toXML and 
    # appends specific nodes for this class
    def toXML(self, dom: minidom.Document) -> minidom.Node:
        n_node = super().toXML(dom)

        defaultfloatnode = dom.createElement("default-float")
        defaultfloatnode.setAttribute("type","float")
        valueText = dom.createTextNode(str(self.getDefaultData()))
        defaultfloatnode.appendChild(valueText)
        n_node.appendChild(defaultfloatnode)

        rangeminnode = dom.createElement("rangemin")
        rangeminnode.setAttribute("type","float")
        valueText = dom.createTextNode(str(self.getMin()))
        rangeminnode.appendChild(valueText)
        n_node.appendChild(rangeminnode)

        rangemaxnode = dom.createElement("rangemax")
        rangemaxnode.setAttribute("type","float")
        valueText = dom.createTextNode(str(self.getMax()))
        rangemaxnode.appendChild(valueText)
        n_node.appendChild(rangemaxnode)
        
        return n_node

    # Creates the object instance from an XML node
    def fromXML(n_node: minidom.Node, pdoc: PORISDoc) -> PORISValueFloat:
        ret = super(PORISValueFloat,PORISValueFloat).fromXML(n_node, pdoc)
        ret.__class__ = PORISValueFloat

        defaultfloatnode = n_node.getElementsByTagName('default-float')[0]
        if (defaultfloatnode is None):
            print("ERROR! default float is None")
            
        else:
            for t in defaultfloatnode.childNodes:
                if t.nodeType == t.TEXT_NODE:
                    ret.setDefaultData(float(t.nodeValue))
            
        minnode = n_node.getElementsByTagName('rangemin')[0]
        if (minnode is None):
            print("ERROR! default float is None")
            
        else:
            for t in minnode.childNodes:
                if t.nodeType == t.TEXT_NODE:
                    ret.__min = float(t.nodeValue)            
            
        maxnode = n_node.getElementsByTagName('rangemax')[0]
        if (maxnode is None):
            print("ERROR! default float is None")
            
        else:
            for t in maxnode.childNodes:
                if t.nodeType == t.TEXT_NODE:
                    ret.__max = float(t.nodeValue)            
            
        formatter = PORISValueFormatter.fromXMLRef(n_node)
        ret.setXMLFormatter(formatter)
        
        return ret

#######################################
# This class implements the PORIS Modes
# PORISModes are used to restrict the eligible values for a PORISParam
# or to restrict the eligible submodes for a PORISSys

# As we need to use the class from the class itself, we will need to declare it in advance
class PORISMode(PORIS):
    pass

# This is the actual definition of the class
class PORISMode(PORIS):
    
    # Constructor, uses super()'s an adds the initialization of the eligible values and submodes
    def __init__(self,name):
        super().__init__(name)
        self.values = {}
        self.submodes = {}
        self.__default_value = None
        
    # Function o add a submode as eligible if current mode is active
    def addSubMode(self,m: PORISMode):
        self.submodes[m.id] = m

    # Function o add a value as eligible if current mode is active
    def addValue(self,v: PORISValue):
        self.values[v.id] = v
        # If there is no default value of this mode, this will be 
        # the first default value
        if self.__default_value == None:
            self.__default_value = v
    
    # Setter for the default value
    def setDefaultValue(self, v: PORISValue) -> PORISValue:
        ret = self.__default_value
        if (v.id in self.values):
            # Setting the candidate as the default value
            self.__default_value = v
            ret = v
            
        else:
            print("Error, we can not set a default value",v.getName(),"which is not in the list of values for this mode")
    
        return ret
    
    # Getter for the default value
    def getDefaultValue(self) -> PORISValue:
        return self.__default_value
        
    # Gets the most suitable value from the list of eligible ones.
    # The arguments are accepting a candidate and a current value
    # if the candidate value is eligible, then it will be returned
    # otherwise if the current value is eligible, then it will be returned
    # if none of them both were returned, then the first eligible value will be returned
    # This method plays an inportant role when changes are made at higher levels
    # of the PORIS tree, helping the subtree to arrive to a consistent state
    # propagating the change to eligible values in case the triggering changes 
    # make the tree inconsitent.
    def getEligibleValue(self,v,current) -> PORISValue:
        if debug:
            if (v != None):
                print("Entering in PORISMode getEligibleValue for mode", self.getName(), "with the candidate", v.getName())
            else:
                print("Entering in PORISMode getEligibleValue for mode", self.getName(), "with NULL candidate")
    
            print("Eligible valeus for this mode",self.values.keys())

        ret = None
        if v.id in self.values.keys():
            # The candidate was found in the eligible ones
            ret = v

        else:
            # The candidate was not found in the eligible ones
            if current.id in self.values.keys():
                # The current value was found in the eligible ones
                ret = current
            
            else:
                # Neither the candidate nor the current values were eligible
                # We will return the default value, which is always eligible
                ret = self.__default_value

        return ret
    
    # Gets the most suitable submode from the list of eligible ones.
    # The arguments are accepting a candidate and a current submode
    # if the candidate submode is eligible, then it will be returned
    # otherwise if the current submode is eligible, then it will be returned
    # if none of them both were returned, then the first eligible submode will be returned
    # This method plays an inportant role when changes are made at higher levels
    # of the PORIS tree, helping the subtree to arrive to a consistent state
    # propagating the change to eligible submodes in case the triggering changes 
    # make the tree inconsitent.
    # Important: canddate(m) and current submodes shall belong to the same parent item (param or sys)
    # Take into account that submodes list is mixing modes of several items.
    # Finally, if there is no eligible submode belonging to the same parent that the m mode, the UNKNOWN mode
    # mode of m's parent.  UNKNOwN modes disables the parent item, and this is the method which
    # allows disabling parts of a PORIS subtree depending on the choices made at higher levels
    # TODO: Implement a check to confirm m and current are siblings
    def getEligibleSubMode(self,m,current) -> PORISMode:
        if debug:
            if m != None:
                print("Entering in PORISMode getEligibleSubMode with mode", self.getName(), "with the candidate", m.getName())

            else:
                print("Entering in PORISMode getEligibleSubMode with mode", self.getName(), "with NULL candidate")

            print("Eligible submodes:",self.submodes.keys())

        ret = None
        if m.id in self.submodes.keys():
            # The candidate was found in the eligible ones
            ret = m
        
        else:
            # The candidate was not found in the eligible ones
            if current.id in self.submodes.keys():
                # The current value was found in the eligible ones
                ret = current
                
            else:
                # We will try to find the default mode for the PORISNode holding the candidate mode
                defmode = m.getParent().getDefaultMode()
                if defmode.id in self.submodes.keys():
                    ret = defmode
                    
                else:
                    if debug:
                        print("None of the two given or the default one, I have only these keys",self.submodes.keys())

                    # Neither the candidate nor the current submodes were eligible
                    # Search the first submode with the same parent than the candidate
                    # Iterating all submodes
                    for ks in self.submodes.keys():
                        s = self.submodes[ks]
                        if debug:
                            print(s.getParent(),s.getParent().getName())

                        # Selecting the current submode only if it shares parent with candidate mode (m)
                        if s.getParent() == m.getParent():
                            ret = s
                            # We found the first valid item to return
                            # We shall exit breaking the loop 
                            break
                    
                    if ret is None:
                        # We finanly did not found an eligible submode for this mode, for the PORISNode item which is parent of m
                        # So we will return the UNKNOWN mode (the first one of the item)
                        ret = m.getParent().modes[list(m.getParent().modes.keys())[0]]

        return ret
    
    # This functions executes getEligibleValue() using an index to select the candidate
    # It also returns an index
    def getEligibleValueFromIdx(self,idx,current) -> PORISValue:
        vk = list(self.values.keys())[idx]
        result = self.getEligibleValue(self.values[vk],current)
        if result is None:
            ret = 0
        else:
            ret = result.idx
        
        return ret

    # This functions executes getEligibleSubMode() using an index to select the candidate
    # It also returns an index
    def getEligibleSubModeFromIdx(self,idx,current) -> int:
        mk = list(self.submodes.keys())[idx]
        result = self.getEligibleSubMode(self.submodes[mk],current)
        if result is None:
            ret = 0
        else:
            ret = result.idx
        
        return ret
    
    # Getter for PORISMode destinations, which can be values or submodes
    def getDestinations(self) -> list:
        ret = []
        for k in self.values:
            ret.append(self.values[k])

        for k in self.submodes:
            ret.append(self.submodes[k])
            
        return ret
    
    ########### XML related functions ########

    # Getter for the XML tag name of this item
    def getXMLNodeName(self) -> str:
        return "poris-mode"
    
    # Getter for the NodeType of this item
    def getXMLNodeType(self) -> int:
        return 6
    
    # Dumps the XML node from this PORISMode
    # It uses super's function, and adds the default mode and default value
    # TODO: Implement the default mode and default value, at this moment we are 
    # dumping them as NIL, just for consistency with porisjava's XML
    def toXML(self, dom: minidom.Document) -> minidom.Node:
        '''
        <default-mode-id type="integer" nil="true"/>
        <default-value-id type="integer" nil="true"/>
        '''            
        n_node = super().toXML(dom)
        # TODO: Think if it makes sense to have a default submode???
        defaultmodenode = dom.createElement("default-mode-id")
        defaultmodenode.setAttribute("type","integer")
        defaultmodenode.setAttribute("nil","true")
        n_node.appendChild(defaultmodenode)
        defaultvaluenode = dom.createElement("default-value-id")
        defaultvaluenode.setAttribute("type","integer")
        v = self.getDefaultValue()
        if v is None:
            defaultvaluenode.setAttribute("nil","true")
            
        else:
            defaultvaluetext = dom.createTextNode(str(v.id))
            if defaultvaluetext is not None:
                defaultvaluenode.appendChild(defaultvaluetext)
                
            else:
                print("Error creating a text node for the default value of the",self.getName(),"mode")
                assert(False)
            
        n_node.appendChild(defaultvaluenode)
        
        return n_node

    # Creates the object instance from an XML node
    def fromXML(n_node: minidom.Node, pdoc: PORISDoc) -> PORISMode:
        ret: PORISMode
        ret = super(PORISMode,PORISMode).fromXML(n_node, pdoc)
        ret.__class__ = PORISMode
        # TODO: Parse these values
        ret.values = {}
        ret.submodes = {}
        ret.__default_value = None
        
        return ret

    
#######################################
# This class is the base one for PORISParam and PORISSys

# This is the actual definition of the class
class PORISNode(PORIS):
    # Constructor, creates the modes dictionary
    def __init__(self,name):
        super().__init__(name)
        # A PORISNode has a selected mode 
        self.__selectedMode = None
        self.modes = {}
        self.__defaultMode = None
    
    # This function adds a mode to the current item
    # If there is no mode selected, the first one is 
    # then considered as selected
    # Note: In our initialization we always add the UNKNONW mode, without submodes, in the first position
    # this is the mechanism to disable a POrISNOde (and all its subtree) when none of its submodes is eligible
    # NOTE: We should consider creating and adding the UNKNOWN mode in the constructor of the item, to don't let the user
    # violate the restriction written here, and add an alternative mode as the first one
    def addMode(self,m):
        self.modes[m.id] = m
        m.setParent(self)
        if self.__defaultMode == None:
            # No mode was the default one, this one will be the default one
            self.__defaultMode = m

        if self.__selectedMode == None:
            # No mode was selected, this one will be the selected one
            self.__selectedMode = m

    # Getter for the default mode
    def getDefaultMode(self) -> PORISMode:
        return self.__defaultMode
    
    # Setter for the default mode
    def setDefaultMode(self, m:PORISMode) -> PORISMode:
        print("Setting ",m.getName(),"as the default mode for",self.getName())
        if m.id in self.modes.keys():
            self.__defaultMode = m
            
        else:
            print("Error, ", m.getName(), "is not one of", self.getName(), "modes")
        
        return self.__defaultMode
    
    # Getter for the selected mode
    def getSelectedMode(self) -> PORISMode:
        return self.__selectedMode

    # Setter for the selected mode, names as the act of select it
    def selectMode(self, m:PORISMode) -> PORISMode:
        # First we will get an eligible mode givin our candidate
        ret = self.getEligibleMode(m)
        if ret is None:
            if debug:
                print("New eligible mode is NULL, so we have to set initialize the item to select the unknown mode")

            ret = self.init()

        # If the mode has changed from the previous one, we shall propagate the change
        if ret != self.getSelectedMode():
            if debug:
                print("New mode is", ret.getName())
                if self.getSelectedMode() is not None:
                    print (" which is diferent from",self.getSelectedMode().getName())
                else:
                    print(" which is different from NULL")        

            self.__selectedMode = ret

        return ret

    # Setter for the selected mode using an index in the modes list, instead of using the mode itself
    def setModeFromIdx(self,idx) -> int:
        success = False
        # First we find the mode using the index
        mk = list(self.modes.keys())[idx]
        if mk is not None:
            result = self.selectMode(self.modes[mk])
            if result is not None:
                # We succeeded in setting the mode using the index
                ret = result.idx
                success = True
                
        if not success:
            # We could not set the mode using the idx
            # so we will initialize the item to select the UNKNOWN mode
            result = self.init()
            # index for UNKNOWN is 0
            ret = 0

        return ret

    # In case an item has not a selected mode, we can use this function to 
    # select the first node
    # This function is normally only called internally, in reaction to
    # the circumstances of not having a selected mode when it is expected to have
    def init(self) -> PORISMode:
        if debug:
            print("----> Init ",self.getName(),", mode list len:" , len(self.modes))

        # We select the first mode of the list, and set it as the selected one
        firstMode = self.modes[list(self.modes.keys())[0]]
        self.__selectedMode = firstMode
        if debug:
            print("Init ", self.getName() + ":",firstMode.getName())

        return self.__selectedMode
    
    # This function gets the selected mode of a PORISNode.  In case there is no selected mode
    # it forces the selection of the first one (UNKNOWN)
    def getNotNullSelectedMode(self) -> PORISMode:
        if debug:
            print("Entering in PORISNode getNotNullSelectedMode", self.getName())

        ret = self.getSelectedMode()
        if ret is None:
            # There is no selected mode?  Then we will force the item initialization
            # This normally is not occurring, because from the first mode added, the item
            # has a selected one
            if debug:
                print("- selectedMode is NULL")
            
            # If there is no selected mode, we will initialize the item, which will select 
            # the first mode as the active one (the first mode should be the UNKNOWN one)
            ret = self.init()
            
        if debug:
            print("- selectedMode es now", self.getSelectedMode().getName())
        # This looks like redundant, but it is not!!!
        return self.selectMode(self.getSelectedMode())


    # Gets the most suitable mode from the list of eligible ones for this item.
    # The argument is a candidate mode
    # if the candidate submode is eligible, then it will be returned
    # otherwise if the current submode is eligible, then it will be returned
    # if none of them both were returned, then the first eligible submode will be returned
    # This method plays an inportant role when changes are made at higher levels
    # of the PORIS tree, helping the subtree to arrive to a consistent state
    # propagating the change to eligible submodes in case the triggering changes 
    # make the tree inconsitent.
    # Important: canddate(m) and current submodes shall belong to the same parent item (param or sys)
    # Take into account that submodes list is mixing modes of several items.
    # Finally, if there is no eligible submode belonging to the same parent that the m mode, the UNKNOWN mode
    # mode of m's parent.  UNKNOwN modes disables the parent item, and this is the method which
    # allows disabling parts of a PORIS subtree depending on the choices made at higher levels
    # TODO: Implement a check to confirm m and current are siblings
    def getEligibleMode(self,m) -> PORISMode:
        if debug:
            print("Entering in PORISNode ",self.getName(), ".getEligibleMode("+m.getName()+")")

        ret = None
        if m.id in self.modes.keys():
            # m is a mode of the current item
            if self.getParent() is None:
                # Current item has no parent, no restrictions to set m
                if debug:
                    print("Parent of", self.getName(), "is null, no upper levels for restrictions, we can freely select m")

                ret = m
            
            else:
                # As this mode has a parent, we need to select a mode which is elegible in the context of the active mode at higher level
                # presenting the candidate as the candidate one, and the current mode as the alternative candidate
                if debug:
                    print("Searching within the", len(self.getParent().getSelectedMode().submodes),"submodes of",self.getParent().getName())
                    print("selectedMode",self.getSelectedMode().getName(),m.getName())

                ret = self.getParent().getSelectedMode().getEligibleSubMode(m,self.getSelectedMode())

            if ret is None:
                if debug:
                    print("ERROR, we were not lucky, there was no way of selecting a mode (NULL after search")
            
            else:
                if debug:
                    print("Selected mode is",ret.getName())

        else:
            print("ERROR, trying to select",m.getName(),"which is not a mode of",self.getName())
            # We then try to find a suitable mode depending on the choices done at higher level
            # we can not present m as a candidate, so we are presenting the current selected mode as candidate too
            if self.getParent() is None:
                # No parent, we can select the default mode
                ret = self.__defaultMode
    
            else:
                ret = self.getParent().getSelectedMode().getEligibleSubMode(self.getSelectedMode(), self.__defaultMode)
        
        return ret


    # Function to get an elegible mode using an index
    def getEligibleModeFromIdx(self,idx) -> int:
        ret = 0

        mk = list(self.modes.keys())[idx]
        if mk is not None:
            result = self.getEligibleMode(self.submodes[mk])
            if result is not None:
                ret = result.idx
                success = True
     
        return ret

    # Get a mode from its Idx
    def getModeFromId(self,myid) -> PORISMode:
        ret = None
        if myid in self.modes.keys():
            ret = self.modes[myid]

        return ret        

    # Get a mode from its name
    def getModeFromName(self,myname) -> PORISMode:
        ret = None
        for myid in self.modes.keys():
            if self.modes[myid].getName() == myname:
                ret = self.modes[myid]

        return ret

    # Getter for the destinations list, including the modes
    def getDestinations(self) -> list:
        ret = []
        for k in self.modes:
            ret.append(self.modes[k])
            
        return ret

    ########### XML related functions ########

    # Function to obtain the tag name for the current item
    # In XML all PORISNodes (no mather if they are systems or params)
    # are <sub-system>
    def getXMLNodeName(self) -> str:
        return "poris-node"
    
    # Function to obtain the NodeType, overloading super's
    def getXMLNodeType(self) -> int:
        return 4
    
    # Dump XML from this item.  Appends default mode
    # to super's XML
    # TODO: At the moment we have not selected default modes
    def toXML(self, dom: minidom.Document) -> minidom.Node:
        '''
        <default-mode-id type="integer" nil="true"/>
        '''            
        n_node = super().toXML(dom)
        defaultmodenode = dom.createElement("default-mode-id")
        defaultmodenode.setAttribute("type","integer")
        # WARNING: It looks like the java panel is not correctly using default mode

        m = self.getDefaultMode()
        if m is None:
            defaultmodenode.setAttribute("nil","true")
            
        else:
            defaultmodetext = dom.createTextNode(str(m.id))
            if defaultmodetext is not None:
                defaultmodenode.appendChild(defaultmodetext)
                
            else:
                print("Error creating a text node for the default value of the",self.getName(),"mode")
                assert(False)
            
        n_node.appendChild(defaultmodenode)        
        
        
        return n_node    

    # Creates the object instance from an XML node
    def executeXMLParser(n_node: minidom.Node, pdoc: PORISDoc) -> PORISNode:
        typenode: minidom.Node = n_node.getElementsByTagName("type")[0]
        t = typenode.firstChild.nodeValue
        if t == "PORISParam":
            return PORISParam.fromXML(n_node, pdoc)

        else:
            if t == "PORISSys":
                return PORISSys.fromXML(n_node, pdoc)


        # Let's see the destinations to know if it is a PORISSys or a PORISParam
        destnode: minidom.Node = n_node.getElementsByTagName("destinations")[0]
        for d in destnode.childNodes:
            if d.getAttribute("type") == "PORISNode" or d.getAttribute("type") == "PORISSys" or d.getAttribute("type") == "PORISParam":
                return PORISSys.fromXML(n_node, pdoc)
                
        return PORISParam.fromXML(n_node, pdoc)

    def fromXML(n_node: minidom.Node, pdoc: PORISDoc) -> PORISNode:
        ret = super(PORISNode,PORISNode).fromXML(n_node, pdoc)
        ret.__class__ = PORISNode
        ret.modes = {}
        ret.__defaultMode = None

        return ret


#######################################
# This class implements a param, which is a PORISNode which has values 
# and does not have subsystems or subparams
class PORISParam(PORISNode):
    pass

class PORISParam(PORISNode):  
    # Constructor, it adds values to superclass
    def __init__(self,name):
        self.__selectedValue = None  # Current selected value for the param
        super().__init__(name)
        self.values = {}
  
    # Getter for the selected value
    def getSelectedValue(self) -> PORISValue:
        return self.__selectedValue
    
    # Function to add a value.
    # If it is the first value added, it also will be the selected one
    def addValue(self,v):
        self.values[v.id] = v
        v.setParent(self)
        if self.__selectedValue == None:
            self.__selectedValue = v

    # Sets an elegible value, by trying to re-select the current one
    # if the current value is not elegible, setValue will find another one
    # It returns the finally selected value
    def setEligibleValue(self) -> PORISValue:
        if debug:
            print("Entro en PORISParam setEligibleValue", self.getName())

        return self.setValue(self.__selectedValue)
    
    # Selects a mode, if it is elegible
    def selectMode(self,m) -> PORISMode:
        if debug:
            print("Entering in PORISParam",self.getName()+".selectMode("+ m.getName()+"\")")

        prev_mode = self.getSelectedMode()
        ret = super().selectMode(m)
        
        if ret != prev_mode:
            # The mode has changed, so we have to set a consistent value
            # Once the new mode is selected, we shoult set an elegible value by trying to re-select the current one
            self.setValue(self.getSelectedValue())

        return ret

    # Getter for value using the ID
    def getValueFromId(self,myid) -> PORISValue:
        ret = None
        if myid in self.values.keys():
            ret = self.values[myid]

        return ret

    # Getter for value using the name
    def getValueFromName(self,myname) -> PORISValue:
        ret = None
        for myid in self.values.keys():
            if self.values[myid].getName() == myname:
                ret = self.values[myid]

        return ret

    # Gets an elegible value, presenting a candidate (v) and an alternative (current)
    def getEligibleValue(self,v,current) -> PORISValue:
        if debug:
            if v is None:
                print("Entering in PORISParam getEligibleValue ", self.getName(), "with NULL value")
            else:
                print("Entering in PORISParam getEligibleValue ", self.getName(), "with value", v.getName())

            print("***",self.getName(),self.getSelectedMode().getName(),self.modes)

        ret = None
        
        # First obtain the selected mode to know the elegible ones
        if self.getSelectedMode() is None:
            if debug:
                print("- selectedMode is NULL")
            # If there is no selected mode, let's initialize the item
            self.init()

        # Now let`s set the value by get an elegible one from the selected mode, proposing the candidate or the current one as alternative
        ret = self.getSelectedMode().getEligibleValue(v,current)
        
        return ret

    # Setter for the value
    def setValue(self,v) -> PORISValue:
        if debug:
            if v is None:
                print("Entering in PORISParam setValue", self.getName(), "with NULL value")
            else:
                print("Entering in PORISParam setValue", self.getName(), "with value", v.getName())

        # First let's try to see if the candidate is elegible, givin the current one as the alternative
        ret = self.getEligibleValue(v,self.__selectedValue)
        # if the value was already set, no changes have to be executed
        # but if the eligible value is not the selected one, we must apply the eligible value
        if ret != self.__selectedValue:
            # So we have to apply the change of value

            # First, try to copy the existing data, in case this item contains data
            # (is instance of a PORISValueData class or subclass)
            # print("We are going to apply the value " , ret.getName())
            if isinstance(self.__selectedValue,PORISValueData.__class__):
                # print(ret.getName(),"is a PORISValueData of class", ret.__class__.__name__)
                v = self.__selectedValue
                # print(v.getName())
                # print(ret.getName())
                data = v.getData()
                # data contains the data from the previous value
                # let's try to set the same data on the new value
                ret.setData(data)

            # Then select the new value which will have the same data, or will have rejected it if no eligible
            self.__selectedValue = ret
            
        return ret

    # Getter for eligible value using an index
    def getEligibleValueFromIdx(self,idx :int ,current: PORISValue) -> int:
        ret = 0
        vk = list(self.values.keys())[idx]
        if vk is not None:
            result = self.getEligibleValue(self.values[vk],current)
            if result is not None:
                ret = result.idx

            else:
                print("ERROR, we could not find an elegible value for",self.getName())

        else:
            print("ERROR, the index",idx,"is not valid for selecting a value for",self.getName())

        return ret

    # Value setter using an index
    def setValueFromIdx(self,idx: int) -> int:
        ret = 0
        vk = list(self.values.keys())[idx]
        if vk is not None:
            result = self.setValue(self.values[vk])
            if result is not None:
                ret = result.idx

            else:
                print("ERROR, we could not set a value for",self.getName())
        
        else:
            print("ERROR, the index",idx,"is not valid for selecting a value for",self.getName())

        return ret
    
    # Getter for destinations, appends values to the super's destination
    def getDestinations(self) -> list:
        ret = super().getDestinations()
        for k in self.values:
            ret.append(self.values[k])
            
        return ret
    
    ########### XML related functions ########

    # Function to obtain the type, overrides super's because class name is not used
    # def getXMLType(self) -> str:
    #    return "PORISNode"

    # Dump XML from this item.  Appends default value
    # to super's XML
    # TODO: At the moment we have not selected default values
    def toXML(self, dom: minidom.Document) -> minidom.Node:
        '''
        <default-value-id type="integer" nil="true"/>
        '''            
        n_node = super().toXML(dom)
        childnode = dom.createElement("default-value-id")
        childnode.setAttribute("type","integer")
        childnode.setAttribute("nil","true")
        n_node.appendChild(childnode)
        
        return n_node    

    # Creates the object instance from an XML node
    def fromXML(n_node: minidom.Node, pdoc: PORISDoc) -> PORISParam:
        ret = super(PORISParam,PORISParam).fromXML(n_node, pdoc)
        ret.__class__ = PORISParam
        # TODO: Parse these values
        ret.values = {}
        
        return ret


#######################################
# This class implements a PORIS system, which contain modes 
# and subitems (params or another sub-systems)

# As we need to use the class from the class itself, we will need to declare it in advance
class PORISSys(PORISNode):
    pass

# Here comes the actual definition
class PORISSys(PORISNode):

    # Constructor, which adds the children (params or subsystems)
    # to the attributes provided by superclass PORISNode
    def __init__(self,name):
        super().__init__(name)
        self.params = {}
        self.subsystems = {}

    # Adds a parameters to the parameters dictionary
    def addParam(self,p: PORISParam):
        self.params[p.id] = p
        p.setParent(self)

    # Adds a subsystem to the subsystems diccionary
    def addSubsystem(self,s):
        self.subsystems[s.id] = s
        s.setParent(self)
        
    # This function allows the user to select a mode for the current system
    # It takes a mode candidate and tries to apply it.  If not possible, then 
    # it will return the finally selected mode from the eligible ones
    def selectMode(self,m) -> PORISMode:
        if debug:
            print("Entering in Sys selectMode for", self.getName(), "with candidate mode", m.getName())

        # First we call the select mode function from superclass
        prev_mode = self.getSelectedMode()
        ret = super().selectMode(m)

        # Then, if mode changed, we must propagate the change to the params and subsystems        
        if ret != prev_mode:
            
            # Propagating mode change to params
            for k in self.params.keys():
                p = self.params[k]
                # Propagating the change to the param, by reselecting their current mode if eligible, or forcing a eligible one
                p.getNotNullSelectedMode()

            # Propagating mode changes to subsystems
            for k in self.subsystems.keys():
                s = self.subsystems[k]
                # Propagating the change to the subsystem, by reselecting their current mode if eligible, or forcing a eligible one
                s.getNotNullSelectedMode()
   
        if debug:
            if m == ret:
                print("Candidate mode successfully aplied:", ret.getName())
                
            else:
                if ret != prev_mode:
                    print("Alternative eligible mode applied:",ret.getName())

            print("Exiting PORISSys selectMode for", self.getName(), "with candidate m="+m.getName(), "and result =",ret.getName())

        return ret

    # Getter to obtain a subsystem using the id
    def getParamFromId(self,myid) -> PORISParam:
        ret = None
        if myid in self.params.keys():
            ret = self.params[myid]

        return ret
    
    # Get a param using the name
    def getParamFromName(self,myname) -> PORISParam:
        ret = None
        for myid in self.params.keys():
            if (self.params[myid].getName() == myname):
                ret = self.params[myid]

        return ret

    # Getter to obtain a subsystem using the id
    def getSubSystemFromId(self,myid) -> PORISSys:
        ret = None
        if myid in self.subsystems.keys():
            ret = self.subsystems[myid]

        return ret
    
    # Getter to obtain a subsystem using the name
    def getSubSystemFromName(self,myname) -> PORISSys:
        ret = None
        for myid in self.subsystems.keys():
            if (self.subsystems[myid].getName() == myname):
                ret = self.subsystems[myid]

        return ret     
    
    # Get a descendant PORISParam using an Id
    def getDescendantParamFromId(self,myid) -> PORISParam:
        # First we check the first level of subsystems (children)
        ret = self.getParamFromId(myid)
        if ret is None:
            # If the param is not a children one, we will apply recursivity
            # searching descendants of the children subsystems
            for sk in self.subsystems.keys():
                # Select a child subsystem
                s = self.subsystems[sk]
                # recursive call
                ret = s.getDescendantParamFromID(myid)
                if ret is not None:
                    # found, so we have to return
                    break

            # Recursion end occurs when the descendant is found, or 
            # when we finished looping all the childrens
            
        return ret

    # Get a descendant PORISSys using a name
    def getDescendantParamFromName(self,myname) -> PORISParam:
        # First we check the first level of subsystems (children)
        ret = self.getParamFromName(myname)
        if ret is None:
            # If the subsystem is not a children one, we will apply recursivity 
            # searching descendants of the children ones            
            for sk in self.subsystems.keys():
                # Select a child subsystem
                s = self.subsystems[sk]
                # recursive call
                ret = s.getDescendantParamFromName(myname)
                if ret is not None:
                    # found, so we have to return
                    break
                
            # Recursion end occurs when the descendant is found, or 
            # when we finished looping all the childrens

        return ret

    # Get a descendant PORISSys using an Id
    def getDescendantSysFromId(self,myid) -> PORISSys:
        # First we check the first level of subsystems (children)
        ret = self.getSubSystemFromId(myid)
        if ret is None:
            # If the subsystem is not a children one, we will apply recursivity 
            # searching descendants of the children ones
            for sk in self.subsystems.keys():
                # Select a child subsystem
                s = self.subsystems[sk]
                # recursive call
                ret = s.getDescendantSysFromId(myid)
                if ret is not None:
                    # found, so we have to return
                    break

            # Recursion end occurs when the descendant is found, or 
            # when we finished looping all the childrens
            
        return ret
    
    # Get a descendant PORISSys using an Id
    def getDescendantSysFromName(self,myname) -> PORISSys:
        # First we check the first level of subsystems (children)
        ret = self.getSubSystemFromName(myname)
        if ret is None:
            # If the subsystem is not a children one, we will apply recursivity 
            # searching descendants of the children ones
            for sk in self.subsystems.keys():
                # Select a child subsystem
                s = self.subsystems[sk]
                # recursive call
                ret = s.getDescendantSysFromName(myname)
                if ret is not None:
                    # found, so we have to return
                    break

            # Recursion end occurs when the descendant is found, or 
            # when we finished looping all the childrens
            
        return ret   

    # Getter for destinations
    # It adds subsystems and params to the list
    def getDestinations(self) -> list:
        ret = super().getDestinations()

        for k in self.params:
            ret.append(self.params[k])

        for k in self.subsystems:
            ret.append(self.subsystems[k])
                            
        return ret

    ########### XML related functions ########
    
    # Getter for the type.  In this case the type is not the class name
    # def getXMLType(self) -> str:
    #    return "PORISNode"

    # Creates the object instance from an XML node
    def fromXML(n_node: minidom.Node, pdoc: PORISDoc) -> PORISSys:
        ret = super(PORISSys,PORISSys).fromXML(n_node, pdoc)
        ret.__class__ = PORISSys
        # TODO: Parse these values
        ret.params = {}
        ret.subsystems = {}

        return ret

#######################################
# This class groups a PORIS model inside a "document" with a root
# The intention is to load and save from documents in serialized formats as XML

class PORISDoc:
    
    # Constructor, it needs a project_id to easily identify the document
    def __init__(self,project_id):
        self.__id_counter = 1   # This is the counter for incremental identifiers for the PORIS items inside
        self.__item_dict = {}   # This is a dictionary for accessing easily all the PORIS items by the numeric identifier
        self.__root = None      # This will point to the root system or param in the document
        self.__project_id = project_id  # Sets the given project id
        
    # A setter for the project_id
    def setProjectId(self, i: int):
        self.__project_id = i
        
    # A getter for the project_id
    def getProjectId(self) -> int:
        return self.__project_id
    
    # Sets the given PORIS node (param or sys) as the root for the document
    def setRoot(self, r:PORISNode):
        self.__root = r
        # print("Setting the root to ", r.getName(),"and",self.__root.getName(),"and",self.getName())
        
    # Getter for the root node
    def getRoot(self) -> PORISNode:
        return self.__root        
        
    # Getter for the document's root node name
    def getName(self) -> str:
        return self.__root.getName()
        
    # Adds a PORIS item to the document
    def addItem(self, n: PORIS, id: str=None):
        if id is None:
            # Sets the current counter as the numerical identifier for the item
            n.id = self.__id_counter
            # Increments the id counter
            self.__id_counter += 1
        else:
            n.id = id
        
        # Set the current document as the reference for the id
        n.document = self
        # Adds the item to the item dictionary
        self.__item_dict[str(n.id)] = n

    def getItem(self, i: int) -> PORIS:
        return self.item_dict[str(i)]

    # Prints a list with all the items in the document
    def list_items(self):
        print(len(self.__item_dict))
        for k in self.__item_dict.keys():
            n = self.__item_dict[k]
            print(str(n.id),n.getName())
        
    # Gets a list of PORIS items IDs sorted so their items
    # are never referencing in their destinations a node which has not been 
    # listed before.  This is very convenient, because some consumers of products created
    # from the list - like the PorisGUI panels, which will load the XML created with toXML() -  
    # may have issues if they process items referencing other items which have not been processed before.
    def getConsistentReferencesSortedIdsList(self) -> list:
        node_and_destinations = {}
        for k in self.__item_dict.keys():
            # print(k)
            n = self.__item_dict[k]
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
        
    ########### XML related functions ########        
    
    # Dumps the contents of the PORISDoc into a XML document
    def toXML(self) -> minidom.Document:
        # Creates the XML document
        xmlDocument = minidom.Document()
        
        if xmlDocument is not None:
            # Creates the root tag
            xmlInstr = xmlDocument.createElement('poris')
            if xmlInstr is not None:
                # Appends the root tag to the document
                xmlInstr.setAttribute('id','systems')
                xmlDocument.appendChild(xmlInstr)

                # In order to prevent void references in the consumer, we have to use an ordered list of nodes
                # with no back-references
                consistent_list = self.getConsistentReferencesSortedIdsList()
                
                # We will serialize the items in the XML document using the order in the consistent list
                for id in consistent_list:
                    # Selects the item to dump to an XML node
                    n = self.__item_dict[str(id)]
                    # Calls the XML dumper function for the item
                    n_node = n.toXML(xmlDocument)
                    if (n_node == None):
                        print("ERROR: trying to dump",n.getName(),"to XML node")
                        
                    else:
                        # If success, append the node to the root node of the document
                        xmlInstr.appendChild(n_node)
                        
            else:
                print("ERROR: trying to dump",self.getName(),"we could not create the root tag")
            
        else:
            print("ERROR: trying to dump",self.getName(),"we could not create the XML document object")
            
        # Returning the XML document
        return xmlDocument
        
    # Creates the object instance from an XML node
    def fromXML(self, doc: minidom.Document) -> bool:
        ret = False
        rootnode = doc.firstChild
        if rootnode is None:
            print("null!")
        else:
            if rootnode.localName == "poris":
                for ch in rootnode.childNodes:
                    if (ch.localName == "poris-mode"):
                        md = PORISMode.fromXML(ch, self)

                    else:
                        if (ch.localName == "poris-node"):
                            md = PORISNode.executeXMLParser(ch, self)

                        else:
                            if (ch.localName == "poris-value"):
                                md = PORISValue.fromXML(ch, self)

                            else:
                                if (ch.localName == "poris-value-float"):
                                    md = PORISValueFloat.fromXML(ch, self)

                                else:
                                    if (ch.localName == "poris-sys"):
                                        md = PORISSys.fromXML(ch, self)

                                    else:
                                        if (ch.localName == "poris-param"):
                                            md = PORISParam.fromXML(ch, self)

            else:
                print("not parsing")
    
        return ret