# pyPORIS
A set of tools to manipulate PORIS instruments:

* graph2poris.py: Creates a PORIS model in ODS format from a PORIS diagram in GraphML.
* poris2xml.py: Creates a PORIS xml file from a PORIS model in ODS format.

Dependences:

    pip3 install pyexcel_ods
    pip3 install bs4
    pip3 install pathlib
    pip3 install lxml

Usage:

copy config_rm.py.example to config_rm.py
If you want to use cosmoSys (STILL UNDER DEVELOPMENT) set use_rm = True in config_rm.py file
Then you will have to configure your secrets to access to that cosmoSys instance

* python3 graph2poris.py MyDevice.graphml  # A MyDevice.ods file will be created.
* python3 poris2xml.py MyDevice.ods        # A MyDevice.xml file will be created.





