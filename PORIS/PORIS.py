debug = False

from xml.dom import minidom

class PORISNode:
    pass

class PORIS:
    id = None
    ident = None
    __name = None
    description = None
    __parent = None
    
    def __init__(self,name):
        self.__name = name

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str) -> str:
        self.__name = name

    def setParent(self, parent: PORISNode):
        self.__parent = parent
        
    def getParent(self) -> PORISNode:
        return self.__parent
    
    def toXML(self, dom: minidom.Document) -> minidom.Node:
        n_node = dom.createElement("id_"+str(self.id))
        n_node.setAttribute("name", self.getName())
        
        return n_node

        
class PORISValue(PORIS):
    pass
    

class PORISValueData(PORISValue):
    __data = None
    __default_data = None
    
    def __init__(self,name,default_data):
        super().__init__(name)
        self.__default_data = default_data
        self.__data = default_data

    def setData(self,data):
        self.__data = data
        return self.__data

    def getData(self):
        return self.__data
    
    def getDefaultData(self):
        return self.__default_data

class PORISValueString(PORISValueData):
    def __init__(self,name,default_data: str):
        super().__init__(name,default_data)

    def setData(self,data: str):
        return super().setData(data)

    def getData(self) -> str:
        return super().getData()


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


class PORISMode(PORIS):
    
    def __init__(self,name):
        super(PORISMode, self).__init__(name)
        self.values = {}
        self.submodes = {}
        
    def addSubMode(self,m):
        self.submodes[m.id] = m

    def addValue(self,v):
        self.values[v.id] = v
    
    def getEligibleValue(self,v,current):
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
            print("Estoy en",self.name)
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
            if isinstance(self.__selectedValue,PORISValueData):
                v = self.__selectedValue
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


class PORISDoc:
    __id_counter = 1
    __node_list = []
    __root = None
    
    def setRoot(self, r:PORIS):
        self.__root = r
        print("Setting the root to ", r.getName(),"and",self.__root.getName(),"and",self.getName())
        
    def getRoot(self) -> PORIS:
        return self.__root        
        
    def getName(self):
        return self.__root.getName()
        
    def addNode(self, n: PORIS):
        self.__node_list.append(n)
        n.id = self.__id_counter
        self.__id_counter += 1

    def list_nodes(self):
        for n in self.__node_list:
            print(str(n.id),n.getName())
            
    def toXML(self) -> minidom.Document:
        rootInstr = minidom.Document()
        xmlInstr = rootInstr.createElement('poris')
        rootInstr.appendChild(xmlInstr)
        for n in self.__node_list:
            n_node = n.toXML(rootInstr)
            xmlInstr.appendChild(n_node)
            
        return rootInstr
        