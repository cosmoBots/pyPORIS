from osirisPORIS import *

class osiris_physical(osirisPORIS):
    dummy = "You should override the action triggers here"
    # Go to ARCGengIIIPORIS.py, navigate to the ##### Action triggers ##### section
    # which is normally at the bottom of the class, and copy here the methods 
    # to start overriding them, in order to convert the virtual device into a physical one
    # Once this class has any content, remove the dummy attribute

    ## Action trigger DAS_acquire ##
    def execDAS_acquire(self, value: bool) -> bool:
        # Override this
        return True


    ## Action trigger DAS_abort ##
    def execDAS_abort(self, value: bool) -> bool:
        # Override this
        return True


thismodel = osiris_physical()

print("Let's test our model ",thismodel.root.name)
print("Current mode is ",thismodel.root.selectedMode.name)
print("Current exposuretime value is",thismodel.get_ExpTime().name)
# print("Current exposuretime is",thismodel.get_ExpTimeDouble())

thismodel.set_OsirisMode(thismodel.mdOsirisMode_Imaging)
print("Current mode is ",thismodel.root.selectedMode.name)
value = thismodel.get_ExpTime()
print("Current exposuretime value is",value.name)
print("Current exposuretime is",thismodel.get_ExpTimeDouble())
print("Current exposuretime is",value.getData())
