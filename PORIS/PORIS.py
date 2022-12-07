debug = False

class PORISNode:
    pass

class PORIS:
    __id = None
    __idx = None
    __ident = None
    __name = None
    __description = None
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
            print("Applying", data, "name:", self.__name, "min:", self.__min, "max:", self.__max)

        if data >= self.__min:
            if data <= self.__max:
                return super().setData(data)
                
        return self.__data

    def getData(self) -> float:
        return super().getData()


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
                print("Entro en PORISMode getEligibleValue para el modo", self.name, "con valor propuesto", v.name)
            else:
                print("Entro en PORISMode getEligibleValue para el modo", self.name, "con valor propuesto NULO")
    
            print(self.values.keys())

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
            print("Entro en PORISMode getEligibleSubMode para el modo", self.name, "con m =", m.name)

        ret = None
        found = False

        if debug:
            print(self.submodes.keys())

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
                        print(s.__name,s.__parent.__name)

                    if s.__parent == m.__parent:
                        ret = s
                        break
                
                if ret is None:
                    # None of the given or applicable, I have to apply the first (UNKNOWN mode)
                    ret = m.__parent.modes[list(m.__parent.modes.keys())[0]]
                

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
        m.__parent = self
        if self.__selectedMode == None:
            self.__selectedMode = m

    def init(self):
        if debug:
            print("Init de",self.name,", número de modos:" , len(self.modes))

        firstMode = self.modes[list(self.modes.keys())[0]]
        if debug:
            print("Init ", self.name + ":",firstMode.name)

        self.__selectedMode = firstMode
    
    def setEligibleMode(self):
        if debug:
            print("Entro en PORISNode setEligibleMode", self.__name)

        if self.__selectedMode is None:
            if debug:
                print("- selectedMode es NULO")

            self.init()
            
        if debug:
            print("- selectedMode es ahora", self.__selectedMode.__name)

        # TODO: Check if this selectMode is redundant
        return self.selectMode(self.__selectedMode)

    def selectMode(self,m):
        return None

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
            print("Entro en PORISNode ",self.name, ".getEligibleMode("+m.name+")")

        ret = None
        if self.getParent() is None:
            if debug:
                print("El padre de", self.name, "es nulo")

            ret = m
        
        else:
            if debug:
                print("Buscamos entre los", len(self.__parent.getSelectedMode().submodes),"submodos de",self.__parent.name)
                print("selectedMode",self.__selectedMode.name,m.name)

            ret = self.__parent.__selectedMode.getEligibleSubMode(m,self.__selectedMode)

        if ret is None:
            if debug:
                print("No hubo suerte, el modo a seleccionar es nulo")
        
        else:
            if debug:
                print("El modo seleccionado es",ret.name)
        
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
            if self.modes[myid].name == myname:
                ret = self.modes[myid]

        return ret

    def getSelectedMode(self) -> PORISMode:
        return self.__selectedMode


class PORISParam(PORISNode):
    selectedValue = None
  
    def __init__(self,name):
        super(PORISParam, self).__init__(name)
        self.values = {}
  
    def addValue(self,v):
        self.values[v.id] = v
        v.__parent = self
        if self.selectedValue == None:
            self.selectedValue = v

    def setEligibleValue(self):
        if debug:
            print("Entro en PORISParam setEligibleValue", self.name)

        return self.setValue(self.selectedValue)
    
    def selectMode(self,m):
        if debug:
            print("Entro en Param",self.name+".selectMode("+ m.name+"\")")

        ret = self.getEligibleMode(m)

        if debug:
            print("Estoy en",self.name)
            print(list(self.modes.keys()))

        if ret is None:
            mk = list(self.modes.keys())[0]
            ret = self.modes[mk]

        if ret != self.__selectedMode:
            self.__selectedMode = ret
            self.setValue(self.selectedValue)

        return ret

    def getValueFromId(self,myid):
        ret = None
        if myid in self.values.keys():
            ret = self.values[myid]

        return ret

    def getValueFromName(self,myname):
        ret = None
        for myid in self.values.keys():
            if self.values[myid].name == myname:
                ret = self.values[myid]

        return ret


    def getEligibleValue(self,v,current):
        if debug:
            if v is None:
                print("Entro en PORISParam getEligibleValue ", self.name, "con valor NULO")
            else:
                print("Entro en PORISParam getEligibleValue ", self.name, "con valor", v.name)

            print("***",self.name,self.__selectedMode.__name,self.modes)

        ret = None
        
        if self.__selectedMode is None:
            if debug:
                print("- selectedMode es NULO")

            self.init()

        ret = self.__selectedMode.getEligibleValue(v,current)
        
        return ret

    def setValue(self,v):
        if debug:
            if v is None:
                print("Entro en PORISParam setValue", self.name, "con valor NULO")
            else:
                print("Entro en PORISParam setValue", self.name, "con valor", v.name)

        ret = self.getEligibleValue(v,self.selectedValue)
        if ret != self.selectedValue:
            # First, try to copy the existing data
            if isinstance(self.selectedValue,PORISValueData):
                v = self.selectedValue
                data = v.getData()
                ret.setData(data)

            # Then select the new value
            self.selectedValue = ret
            
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
        p.__parent = self

    def addSubsystem(self,s):
        self.subsystems[s.id] = s
        s.__parent = self
        
    def selectMode(self,m):
        if debug:
            print("Entro en Sys selectMode de", self.name, "con modo", m.name)

        ret = self.getEligibleMode(m)
        if ret is None:
            if debug:
                print("el nuevo modo es NULO que es diferente del seleccionado")
                print(" Hemos de poner el modo UNKNOWN, que por defecto es el primero")

            mk = list(self.modes.keys())[0]
            ret = self.modes[mk]

        if ret != self.getSelectedMode():
            if debug:
                print("el nuevo modo es", ret.name)
                if self.getSelectedMode() is not None:
                    print (" que es diferente de",self.__selectedMode.name)
                else:
                    print(" que es diferente de NULO")

            self.__selectedMode = ret
            
            for k in self.params.keys():
                p = self.params[k]
                p.setEligibleMode()

            for k in self.subsystems.keys():
                s = self.subsystems[k]
                s.setEligibleMode()
   
        else:
            if debug:
                print("el modo escogido es el mismo", ret.name)

        if debug:
            print("Salgo de Sys selectMode de", self.name, "con m="+m.name, "y resultado =",ret.name)

        return ret

   
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
            if (self.params[myid].name == myname):
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

