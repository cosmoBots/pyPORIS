from BaseClass import BaseClass
from Observer import Observer

class Model(BaseClass):

    def __init__(self, name: str):
        self.__name = name
        self.__observers = []
        self.__notifyFlag = True

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        self.__name = name
        self.notifyObs()

    def isNotifyFlag(self):
        return self.__notifyFlag

    def setNotifyFlag(self, notifyFlag:bool):
        self.__notifyFlag = notifyFlag

    def attach(self,obs:Observer):
        self.__observers.append(obs)

    def detach(self,obs:Observer):
        self.__observers.remove(obs)

    def notifyObs(self):
        if (self.isNotifyFlag()):
            for obs in self.__observers:
                obs.update()

    def toString(self) -> str:
        return self.getName()
    
    def equals(self, obj):
        ret = super().equals(obj)
        if ret == False:
            if isinstance(obj, str):
                ret = self.toString() == obj

        return ret
    
    def clone(self):
        return self.cloneWithName(self.getName())
                                  
    def cloneWithName(self, name: str):
        return Model(name)

'''

m = Model("hola")
print(m.getName())
print(m.toString())
o = Observer()
m.attach(o)
o2 = Observer()
m.attach(o2)
m.notifyObs()

m2 = m.clone()
print(m2.toString())
m3 = m.cloneWithName("Hola2")
print(m3.toString())

m.setName("Cambiado")
print(m.toString())
print(m2.toString())

m.detach(o)
m.notifyObs()

'''