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


############################### PORIS item classes ############################################################

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
    __labels = {}           # A dictionary of labels for this item, the scope_kind acts as a key
    
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

    # Function for adding a label to the labels list.
    # caption is the string to show within a context
    # scope_kind is an identifier of the context where the caption applies
    def addLabel(self, caption: str, scope_kind: str):
        self.__labels[scope_kind] = caption
    
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
    
    # Dumps the current item to an XML node
    # PORIS items, after calling this function using super().toXML(doc), 
    # will add additional nodes which will depend on the class
    def toXML(self, dom: minidom.Document) -> minidom.Node:
        # Tag name will be normally the class name, but it can be overloaded
        # so we use a function to get it
        n_node = dom.createElement(self.getXMLNodeName())
       
        # subnode with an identifying integer
        idChild = dom.createElement('id')
        idChild.setAttribute("type", "integer")
        valueText = dom.createTextNode(str(self.id))
        idChild.appendChild(valueText)
        n_node.appendChild(idChild)
        
        # ubnode with an identifying string
        identChild = dom.createElement('ident')
        valueText = dom.createTextNode(self.ident)
        identChild.appendChild(valueText)
        n_node.appendChild(identChild)
                       
        # subnode with the name of the item
        nameChild = dom.createElement('name')
        valueText = dom.createTextNode(self.getName())
        nameChild.appendChild(valueText)
        n_node.appendChild(nameChild)
        
        # subnode with the node type id
        nodetypeChild = dom.createElement('node-type-id')
        nodetypeChild.setAttribute("type", "integer")
        valueText = dom.createTextNode(str(self.getXMLNodeType()))
        nodetypeChild.appendChild(valueText)
        n_node.appendChild(nodetypeChild)
        
        # subnode with the project id
        nodetypeChild = dom.createElement('project-id')
        nodetypeChild.setAttribute("type", "integer")
        valueText = dom.createTextNode(str(self.getProjectId()))
        nodetypeChild.appendChild(valueText)
        n_node.appendChild(nodetypeChild)
        
        # subnode with the type
        nodetypeChild = dom.createElement('type')
        valueText = dom.createTextNode(self.getXMLType())
        nodetypeChild.appendChild(valueText)
        n_node.appendChild(nodetypeChild)
        
        # array of destinations, containing their XML references
        destinations_node = dom.createElement('destinations')
        dests = self.getDestinations()
        for d in dests:
            destnode = dom.createElement('destination')
            destnode.setAttribute("type", d.getXMLType())
            destnode.appendChild(d.toXMLRef(dom))
            destinations_node.appendChild(destnode)
        
        n_node.appendChild(destinations_node)
        
        # array of node attributes
        # TODO: Implement node attributes
        nodeAttributesChild = dom.createElement('node-attributes')
        n_node.appendChild(nodeAttributesChild)
        
        # array of labels
        
        lbs = self.getLabels()
        '''
        # For testing only, create a label if there not exist
        if len(lbs) == 0:
            self.addLabel(self.getName(),"test")
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
        
        # PORIS items, after calling this function using super().toXML(doc), 
        # will add additional nodes which will depend on the class
        
        return n_node

##################################################
# Base class for all the PORISValue items
# Values may have a formatter associated to it
# if no subclassed, then the item will not take any data
# Users just select the PORISValue and it's done

class PORISValue(PORIS):
    
    ########## XML related functions ########
        
    # the tag name will be "value", but subclasses
    # might overload it
    def getXMLNodeName(self) -> str:
        return "value"
    
    # getter for the node type (overloading PORIS one)
    def getXMLNodeType(self) -> int:
        return 5
    
    def getXMLFormatter(self) -> PORISValueFormatter:
        return PORISVALUEFORMATTER_NIL

    # Dumps the item's XML (uses PORIS superclass' one and appends information of the formatter)
    def toXML(self, dom: minidom.Document) -> minidom.Node:
        n_node = super().toXML(dom)
        n_node.appendChild(self.getXMLFormatter().toXMLRef(dom))
        
        return n_node

    
########################################################
# Base class for the PORISValue items which contain data
# Apart for selecting the PORISValue, user has also to define the data
# data examples are strings, integers, floats, dates, angles, etc.

class PORISValueData(PORISValue):
    __data = None
    __default_data = None
    
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
    
    ########## XML related functions ########
    
    # The tag is "none" because this class shall never
    # be instanced directly
    def getXMLNodeName(self) -> str:
        return "none"

    # The node type is 0 because this class shall never
    # be instanced directly
    def getXMLNodeType(self) -> int:
        return 0

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
    def setData(self,data: str):
        return super().setData(data)

    ########## XML related functions ########

    # getter for the XML tag name
    def getXMLNodeName(self) -> str:
        return "value-string"

    # The node type is 6 for PORISValueStrings
    def getXMLNodeType(self) -> int:
        return 6


#######################################
# This class is a PORISValuestring for storing a filepath
# TODO: Develop this class
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

#######################################
# This class stores Dates in a PORISValueString
# The difference is in the formatter, and 
# in the XML 
# TODO: Develop this class
class PORISValueDate(PORISValueString):

    ########## XML related functions ########
    
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
    __min = None    # Min allowed value for the datum
    __max = None    # Max allowed value for the datum

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
        return "value-double-range"
    
    # getter for the formatter, overload super()'s
    def getXMLFormatter(self) -> PORISValueFormatter:
        return PORISVALUEFORMATTER_REAL

    # Dumps item to XML, uses super().toXML and 
    # appends specific nodes for this class
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
# This class implements the PORIS Modes
# PORISModes are used to restrict the eligible values for a PORISParam
# or to restrict the eligible submodes for a PORISSys
class PORISMode(PORIS):
    
    # Constructor, uses super()'s an adds the initialization of the eligible values and submodes
    def __init__(self,name):
        super(PORISMode, self).__init__(name)
        self.values = {}
        self.submodes = {}
        
    # Function o add a submode as eligible if current mode is active
    def addSubMode(self,m):
        self.submodes[m.id] = m

    # Function o add a value as eligible if current mode is active
    def addValue(self,v):
        self.values[v.id] = v
    
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
                # We will return the first eligible value
                # TODO: Recover the "default value" for a mode
                itk = list(self.values.keys())[0]
                ret = self.values[itk]

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
    def getEligibleSubMode(self,m,current):
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
                if debug:
                    print("None of the two given, I have only these keys",self.submodes.keys())

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
    def getEligibleValueFromIdx(self,idx,current):
        vk = list(self.values.keys())[idx]
        result = self.getEligibleValue(self.values[vk],current)
        if result is None:
            ret = 0
        else:
            ret = result.idx
        
        return ret

    # This functions executes getEligibleSubMode() using an index to select the candidate
    # It also returns an index
    def getEligibleSubModeFromIdx(self,idx,current):
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
        return "mode"
    
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
# This class is the base one for PORISParam and PORISSys
    
class PORISNode(PORIS):
    # A PORISNode has a selected mode 
    __selectedMode = None

    # Constructor, creates the modes dictionary
    def __init__(self,name):
        super(PORISNode, self).__init__(name)
        self.modes = {}
    
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
        if self.__selectedMode == None:
            # No mode was selected, this one will be the selected one
            self.__selectedMode = m

    # Getter for the selected mode
    def getSelectedMode(self) -> PORISMode:
        return self.__selectedMode

    # Setter for the selected mode, names as the act of select it
    def selectMode(self, m:PORISMode):
        if m != None:
            if m.id in self.modes.keys():
                # The mode m is in the list of nodes, we can select it
                self.__selectedMode = m
                return m

            else:
                # The mode could not be set, we return None
                printf("ERROR, the mode",m.getName(),"is not part of the list of modes of",self.getName())
                return None

        else:
            # The mode could not be set, we return None
            printf("ERROR, trying to set None as mode for", self.getName())
            return None

    # Setter for the selected mode using an index in the modes list, instead of using the mode itself
    def setModeFromIdx(self,idx):
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
    def init(self):
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
    def getNotNullSelectedMode(self):
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
    def getEligibleMode(self,m):
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
                    print("El modo seleccionado es",ret.getName())

        else:
            print("ERROR, trying to select",m.getName(),"which is not a mode of",self.getName())
            # We then try to find a suitable mode depending on the choices done at higher level
            # we can not present m as a candidate, so we are presenting the current selected mode as candidate too
            ret = self.getParent().getSelectedMode().getEligibleSubMode(self.getSelectedMode(),self.getSelectedMode())
        
        return ret


    # Function to get an elegible mode using an index
    def getEligibleModeFromIdx(self,idx):
        ret = 0

        mk = list(self.modes.keys())[idx]
        if mk is not None:
            result = self.getEligibleMode(self.submodes[mk])
            if result is not None:
                ret = result.idx
                success = True
     
        return ret

    # Get a mode from its Idx
    def getModeFromId(self,myid):
        ret = None
        if myid in self.modes.keys():
            ret = self.modes[myid]

        return ret        

    # Get a mode from its name
    def getModeFromName(self,myname):
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
        return "sub-system"
    
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
        defaultmodenode.setAttribute("nil","true")
        n_node.appendChild(defaultmodenode)
        
        return n_node    

#######################################
# This class implements a param, which is a PORISNode which has values 
# and does not have subsystems or subparams

class PORISParam(PORISNode):
    __selectedValue = None  # Current selected value for the param
  
    # Constructor, it adds values to superclass
    def __init__(self,name):
        super(PORISParam, self).__init__(name)
        self.values = {}
  
    # Getter for the selected value
    def getSelectedValue(self):
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
    def setEligibleValue(self):
        if debug:
            print("Entro en PORISParam setEligibleValue", self.getName())

        return self.setValue(self.__selectedValue)
    
    # Selects a mode, if it is elegible
    def selectMode(self,m):
        if debug:
            print("Entering in PORISParam",self.getName()+".selectMode("+ m.getName()+"\")")

        # Finds if the candidate is available
        ret = self.getEligibleMode(m)
        if ret is None:
            # The eligible mode returned None, let's initialize this item to select UNKNOWN
            ret = self.init()

        if ret != self.getSelectedMode():
            # The elibible mode is not the selected one, so we have to 
            # select the mode using super() so we do not enter in recursivity
            super(PORISParam,self).selectMode(ret)
            # Once the new mode is selected, we shoult set an elegible value by trying to re-select the current one
            self.setValue(self.__selectedValue)

        return ret

    # Getter for value using the ID
    def getValueFromId(self,myid):
        ret = None
        if myid in self.values.keys():
            ret = self.values[myid]

        return ret

    # Getter for value using the name
    def getValueFromName(self,myname):
        ret = None
        for myid in self.values.keys():
            if self.values[myid].getName() == myname:
                ret = self.values[myid]

        return ret

    # Gets an elegible value, presenting a candidate (v) and an alternative (current)
    def getEligibleValue(self,v,current):
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
    def setValue(self,v):
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
    def getEligibleValueFromIdx(self,idx,current):
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
    def setValueFromIdx(self,idx):
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
    def getXMLType(self) -> str:
        return "PORISNode"

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
                p.getNotNullSelectedMode()

            for k in self.subsystems.keys():
                s = self.subsystems[k]
                s.getNotNullSelectedMode()
   
        else:
            if debug:
                print("el modo escogido es el mismo", ret.getName())

        if debug:
            print("Salgo de Sys selectMode de", self.getName(), "con m="+m.getName(), "y resultado =",ret.getName())

        return ret

    def getNotNullSelectedMode(self):
        if debug:
            print("Entro en PORISSys getNotNullSelectedMode", self.getName())

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
        