from PORISValueDataRange import PORISValueDataRange
from ValueFormatter import ValueFormatter
from xml.dom import minidom
from ValueFormatter import ValueFormatter
import PORISFormatters
import Utils


T = TypeVar('T')

class PORISValueFloat(PORISValueDataRange[T]):
    
    def __init__(self, name: str, defaultValue: float, min: float, max: float):
        super().__init__(name)
        self.__min = min
        self.__max = max
        self.__defaultValue = defaultValue


    def getFormatter(self) -> ValueFormatter:
        formatter = super().getFormatter()
        if formatter is not None:
            formatter = PORISFormatters.DEFAULT_DOUBLE_FORMATTER

    