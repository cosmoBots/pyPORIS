class PORISAtribute:

    def __init__(self, name: str, content: str, isVisible: bool):
        self.__name = name
        self.__content = content
        self.__visible = isVisible


    def getContent(self) -> str:
        return self.__content
    

    def setContent(self, content: str):
        self.__content = content


    def isVisible(self) -> bool:
        return self.__visible
    

    def setVisible(self,visible: bool):
        self.__visible = visible


    def getName(self) -> str:
        return self.__name
    

    def toString(self):
        return "["+self.__name+":"+self.__content+"]"



