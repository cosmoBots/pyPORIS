from typing import TypeVar, Generic, List
from PORISValueData import PORISValueData

T = TypeVar('T')

class PORISValueDataRange(PORISValueData[T]):

    def getMax(self) -> T:
        pass


    def getMin(self) -> T:
        pass

    
    def setMax(self, item: T) -> None:
        pass


    def setMin(self, item: T) -> None:
        pass


