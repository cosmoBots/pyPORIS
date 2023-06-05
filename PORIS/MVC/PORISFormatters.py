from ValueDoubleFormatter import ValueDoubleFormatter
from ValueDateFormatter import ValueDateFormatter
from ValueIntegerFormatter import ValueIntegerFormatter

class PORISFormatters:
    DEFAULT_DOUBLE_FORMATTER = ValueDoubleFormatter("real", 1, "real");
    ANGLE_FORMATTER = ValueDoubleFormatter("angle", 4, "angle");
    S_FORMATTER = ValueDoubleFormatter("s", 5, "s");
    DEFAULT_DATE_FORMATTER = ValueDateFormatter("Date", 6, "dd.MM.yyyy HH:mm:ss z");
    DEFAULT_INTEGER_FORMATTER = ValueIntegerFormatter("integer", 7, "#");
    DEFAULT_STRING_FORMATTER = None;