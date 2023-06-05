from typing import TypeVar, Generic, List
from PORISValue import PORISValue

T = TypeVar('T')

class PORISValueData(PORISValue[T]):

    def setDefaultValue(self, item: T) -> None:
        pass

    def getDefaultValue(self) -> T:
        pass

