from ARCGenIIIPORIS import *

class ARCGenIII_physical(ARCGenIIIPORIS):
    # Go to ARCGengIIIPORIS.py, navigate to the ##### Action triggers ##### section
    # which is normally at the bottom of the class, and copy here the methods 
    # to start overriding them, in order to convert the virtual device into a physical one
    # Once this class has any content, remove the pass clause

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

print("Let's test our model ",thismodel.root.getName())
print("Current mode is ",thismodel.root.getSelectedMode().getName())

thismodel.execARCGenIII_cfg_init_expose(True)
