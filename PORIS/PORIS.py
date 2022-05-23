debug = False

class PORIS:
    myclassname = "PORIS"
    id = None
    idx = None
    ident = None
    name = None
    description = None
    parent = None
    def __init__(self,name):
        self.name = name
        
        
class PORISValue(PORIS):
    myclassname = "PORISValue"
    
class PORISValueFloat(PORISValue):
    myclassname = "PORISValueFloat"
    data = None
    min = None
    max = None
    default_data = None

    def setData(self,floatdata):
        if debug:
            print("Applying", floatdata, "name:", self.name, "min:", self.min, "max:", self.max)

        if floatdata >= self.min:
            if floatdata <= max:
                self.data = floatdata
        
        return self.data

class PORISValueText(PORISValue):
    myclassname = "PORISValueText"
    data = None
    default_data = None
    
    def setData(self,strdata):
        self.data = strdata
        
        return self.data    

class PORISMode(PORIS):
    
    def __init__(self,name):
        super(PORISMode, self).__init__(name)
        self.values = {}
        self.submodes = {}
        
    def addSubMode(self,m):
        self.submodes[m.name] = m

    def addValue(self,v):
        self.values[v.name] = v
    
    def getEligibleValue(self,v,current):
        if debug:
            if (v != None):
                print("Entro en PORISMode getEligibleValue para el modo", self.name, "con valor propuesto", v.name)
            else:
                print("Entro en PORISMode getEligibleValue para el modo", self.name, "con valor propuesto NULO")
    
            print(self.values.keys())

        ret = None
        if v.name in self.values.keys():
            ret = v
        else:
            if current.name in self.values.keys():
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

        if m.name in self.submodes.keys():
            ret = m
        
        else:
            if current.name in self.submodes.keys():
                ret = current
                
            else:
                # If none of two are found, search the first submode with the same parent
                if debug:
                    print("Pruebo aqui",self.submodes.keys())

                for ks in self.submodes.keys():
                    s = self.submodes[ks]
                    if debug:
                        print(s.name,s.parent.name)

                    if s.parent == m.parent:
                        ret = s
                        break

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
    selectedMode = None

    def __init__(self,name):
        super(PORISNode, self).__init__(name)
        self.modes = {}
    
    
    def addMode(self,m):
        self.modes[m.name] = m
        m.parent = self
        if self.selectedMode == None:
            self.selectedMode = m

    def init(self):
        if debug:
            print("Init de",self.name,", número de modos:" , len(self.modes))

        firstMode = list(self.modes.keys())[0]
        if debug:
            print("Init ", self.name + ":",firstMode.name)

        self.setMode(firstMode)    
    
    def setEligibleMode(self):
        if debug:
            print("Entro en PORISNode setEligibleMode", self.name)

        if self.selectedMode is None:
            if debug:
                print("- selectedMode es NULO")

            self.init()
            
        if debug:
            print("- selectedMode es ahora", self.selectedMode.name)

        # TODO: Check if this setMode is redundant
        return self.setMode(self.selectedMode)

    def setMode(self,m):
        return None

    def setModeFromIdx(self,idx):
        mk = list(self.modes.keys())[idx]
        result = self.setMode(self.modes[mk])
        if result is None:
            ret = 0
        else:
            ret = result.idx
        
        if debug:
            print("Acaba la operación setMode con resultado", ret)

        return ret

    def getEligibleMode(self,m):
        if debug:
            print("Entro en PORISNode ",self.name, ".getEligibleMode("+m.name+")")

        ret = None
        if self.parent is None:
            if debug:
                print("El padre de", self.name, "es nulo")

            ret = m
        
        else:
            if debug:
                print("Buscamos entre los", len(self.parent.selectedMode.submodes),"submodos de",self.parent.name)
                print("selectedMode",self.selectedMode.name,m.name)

            ret = self.parent.selectedMode.getEligibleSubMode(m,self.selectedMode)

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

    def getModeFromName(self,name):
        ret = None
        if name in self.modes.keys():
            ret = self.modes[name]

        return ret        


class PORISParam(PORISNode):
    selectedValue = None
  
    def __init__(self,name):
        super(PORISParam, self).__init__(name)
        self.values = {}
  
    def addValue(self,v):
        self.values[v.name] = v
        v.parent = self
        if self.selectedValue == None:
            self.selectedValue = v

    def setEligibleValue(self):
        if debug:
            print("Entro en PORISParam setEligibleValue", self.name)

        return self.setValue(self.selectedValue)
    
    def setMode(self,m):
        if debug:
            print("Entro en Param",self.name+".setMode("+ m.name+"\")")

        ret = self.getEligibleMode(m)

        if debug:
            print("Estoy en",self.name)
            print(list(self.modes.keys()))

        if ret is None:
            mk = list(self.modes.keys())[0]
            ret = self.modes[mk]

        if ret != self.selectedMode:
            self.selectedMode = ret
            self.setValue(self.selectedValue)

        return ret

    def getValueFromName(self,name):
        ret = None
        if name in self.values.keys():
            ret = self.values[name]

        return ret        

    def getEligibleValue(self,v,current):
        if debug:
            if v is None:
                print("Entro en PORISParam getEligibleValue ", self.name, "con valor NULO")
            else:
                print("Entro en PORISParam getEligibleValue ", self.name, "con valor", v.name)

            print("***",self.name,self.selectedMode.name,self.modes)

        ret = None
        
        if self.selectedMode is None:
            if debug:
                print("- selectedMode es NULO")

            self.init()

        ret = self.selectedMode.getEligibleValue(v,current)
        
        return ret

    def setValue(self,v):
        if debug:
            if v is None:
                print("Entro en PORISParam setValue", self.name, "con valor NULO")
            else:
                print("Entro en PORISParam setValue", self.name, "con valor", v.name)

        ret = self.getEligibleValue(v,self.selectedValue)
        if ret != self.selectedValue:
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
        self.params[p.name] = p
        p.parent = self

    def addSubsystem(self,s):
        self.subsystems[s.name] = s
        s.parent = self
        
    def setMode(self,m):
        if debug:
            print("Entro en Sys setMode de", self.name, "con modo", m.name)

        ret = self.getEligibleMode(m)
        if ret is None:
            if debug:
                print("el nuevo modo es NULO que es diferente del seleccionado")
                print(" Hemos de poner el modo UNKNOWN, que por defecto es el primero")

            mk = list(self.modes.keys())[0]
            ret = self.modes[mk]

        if ret != self.selectedMode:
            if debug:
                print("el nuevo modo es", ret.name)
                if self.selectedMode is not None:
                    print (" que es diferente de",self.selectedMode.name)
                else:
                    print(" que es diferente de NULO")

            self.selectedMode = ret
            
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
            print("Salgo de Sys setMode de", self.name, "con m="+m.name, "y resultado =",ret.name)

        return ret

   
    def getSubSystemFromName(self,name):
        ret = None
        if name in self.subsystems.keys():
            ret = self.subsystems[name]

        return ret
    
    def getSubParamFromName(self,name):
        ret = None
        if name in self.params.keys():
            ret = self.params[name]

        return ret
    
    def getDescendantFromName(self,name):
        ret = self.getSubSystemFromName(name)
        if ret is None:
            for sk in self.subsystems.keys():
                s = self.subsystems[sk]
                ret = s.getDescendantFromName(name)
                if ret is not None:
                    break

        return ret
    
    def getDescendantParamFromName(self,name):
        ret = self.getSubParamFromName(name)
        if ret is None:
            print("no es un hijo directo")
            print(name,self.name,self.subsystems)
            for sk in self.subsystems.keys():
                if debug:
                    print(sk)

                s = self.subsystems[sk]
                ret = s.getDescendantParamFromName(name)
                if ret is not None:
                    if debug:
                        print("Tenemos",ret)

                    break

        return ret

