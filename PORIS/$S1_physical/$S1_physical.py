
from DEVICENAMEPORIS import *

class DEVICENAME_physical(DEVICENAMEPORIS):
    dummy = "You should override the action triggers here"
    # Go to ARCGengIIIPORIS.py, navigate to the ##### Action triggers ##### section
    # which is normally at the bottom of the class, and copy here the methods 
    # to start overriding them, in order to convert the virtual device into a physical one
    # Once this class has any content, remove the dummy attribute


thismodel = DEVICENAME_physical()

print("Let's test our model ",thismodel.root.name)
print("Current mode is ",thismodel.root.selectedMode.name)
