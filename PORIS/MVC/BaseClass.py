#!/usr/bin/env python
import sys

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)


# Java to Python by kalkicode.com

class BaseClass(object):

    def isDescendantOf(self, ancestorClass) :
        return issubclass(self.__class__,ancestorClass)
    
    def implementsInterface(self, interfaceClass) :
        return issubclass(self.__class__,interfaceClass)

    @classmethod
    def isClassDescendantOf(cls, clase, ancestorClass):
        return issubclass(clase,ancestorClass)

    @classmethod
    def isClassNameDescendantOf(cls, strClass:str,  ancestorClass) :
        try :
            thisClass = str_to_class(strClass)
            return BaseClass.isClassDescendantOf(thisClass, ancestorClass)
        except Exception as e :
            return False


'''
class TestBaseClass(BaseClass):
    pass


c = TestBaseClass()

print(issubclass(TestBaseClass,BaseClass))
print(c.__class__)
print(issubclass(c.__class__,BaseClass))
print(c.isDescendantOf(BaseClass))
print(BaseClass.isClassDescendantOf(TestBaseClass,BaseClass))
print(BaseClass.isClassNameDescendantOf("TestBaseClass2",BaseClass))
'''
