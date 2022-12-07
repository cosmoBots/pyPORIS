from osirisPORIS import *

class osiris_physical(osirisPORIS):
    # Go to ARCGengIIIPORIS.py, navigate to the ##### Action triggers ##### section
    # which is normally at the bottom of the class, and copy here the methods 
    # to start overriding them, in order to convert the virtual device into a physical one
    # Once this class has any content, remove the pass clause

    ## Action trigger DAS_acquire ##
    def execDAS_acquire(self, value: bool) -> bool:
        # Override this
        return True


    ## Action trigger DAS_abort ##
    def execDAS_abort(self, value: bool) -> bool:
        # Override this
        return True


thismodel = osiris_physical()

print("Let's test our model ",thismodel.root.getName())
print("Current mode is ",thismodel.root.getSelectedMode().getName())
print("Current exposuretime value is",thismodel.get_ExpTime().getName())
thismodel.set_OsirisMode(thismodel.mdOsirisMode_Imaging)
m = thismodel.get_OsirisMode()
print("Current mode is ",m.getName())
value = thismodel.get_ExpTime()
print("Current exposuretime value is",value.getName())
print("Current exposuretime is",thismodel.get_ExpTimeDouble())
print("Current exposuretime is",value.getData())
