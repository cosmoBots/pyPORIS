from ARCGenIIIPORIS import *

class ARCGenIII_physical(ARCGenIIIPORIS):
    dummy = "You should override the action triggers here"
    # Go to ARCGengIIIPORIS.py, navigate to the ##### Action triggers ##### section
    # which is normally at the bottom of the class, and copy here the methods 
    # to start overriding them, in order to convert the virtual device into a physical one
    # Once this class has any content, remove the dummy attribute

    ## Action trigger ARCGenIII_expose ##
    def execARCGenIII_expose(self, value: bool) -> bool:
        print("Expose!!!")
        return True


    ## Action trigger ARCGenIII_init_expose ##
    def execARCGenIII_init_expose(self, value: bool) -> bool:
        print("Init!!!")
        print("Expose!!!")
        return True


    ## Action trigger ARCGenIII_cfg_init_expose ##
    def execARCGenIII_cfg_init_expose(self, value: bool) -> bool:
        print("Config!!!")
        print("Init!!!")
        print("Expose!!!")
        return True


    ## Action trigger ARCGenIII_abort ##
    def execARCGenIII_abort(self, value: bool) -> bool:
        print("Abort!!!")
        return True



thismodel = ARCGenIII_physical()

print("Let's test our model ",thismodel.root.name)
print("Current mode is ",thismodel.root.selectedMode.name)

thismodel.execARCGenIII_cfg_init_expose(True)

