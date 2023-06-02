class ValueFormatter:
    pass

class ValueFormatter:

    __instanceList = []
    
    def __init__(self, name: str, id: int, label:str = None):
        self.__name = name
        self.__label = label
        self.__id = id
        self.__class__.__instanceList.append(self)


    def getId(self) -> int:
        return self.__id
    

    def getName(self) -> str:
        return self.__name
    
    def getLabel(self) -> str:
        return self.__label

    def setLabel(self, label: str):
        self.__label = label

    @classmethod
    def getInstance(cls, name: str) -> ValueFormatter:
        for i in cls.__instanceList:
            if i.getName() == name:
                return i
            
        return None

    @classmethod
    def getInstanceForId(cls, id: int) -> ValueFormatter:
        for i in cls.__instanceList:
            if i.getId() == id:
                return i
            
        return None

