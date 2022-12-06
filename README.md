# pyPORIS

A set of tools to manipulate PORIS instruments:

- porispanel.sh Creates a PORIS representation in ODS and XML format from a PORIS diagram in GraphML, and launches a configuration panel to validate the model.
- porispanel_csys.sh Adds to porispanel.sh the synchronization with a cosmoSys instance.
- porispanel_dir.sh Creates a PORIS representation in an ODS and XML format from a PORIS model which is fragmented in several GraphML files in the same folder.
- odsporispanel.sh Creates a PORIS representation in XML format an launches a configuration panel from an ODS file representing a PORIS model.
- porispanel_dir_csys.sh Adds to porispanel_dir.sh the synchronization with a cosmoSys instance.
- xmlporispanel.sh Launches a configuration panel from a PORIS model representation in XML file.
- redoPorisPython.sh and doPorisPython.sh converts an ODS representation of a PORIS model into convenient Python classes.

The models are taken from the ./models folder and the Python classes are generated inside ./output folder.

## Requirements
- Java
- Python 3
    - pip3 install bs4
    - pip3 install lxml
    - pip3 install pyexcel_ods
    - pip3 install python-redmine

NOTE: In Windows you should use 'pip' instead of 'pip3'

## Preparation after cloning
Execute:

    git submodule update --init --recursive

It will populate pyPORIS folder and the AstroPorisPlayer binaries.

## Converting model to *.ODS, *.XML and open a Java Swing Configuration panel

The PORIS toolkit allows you to convert your model in a GraphML file to models in ODS and XML files.
The ODS file is a representation of the model in an spreadsheet format, useful for later processes like creating Python or C++ classes from it, or importing into cosmoSys.
The XML file is used by the AstroPorisPlayer Java Swing frame app to show an interactive panel to explore/validate your model.
The last step of this conversion process is to show the AstroPorisPlayer panel.

The model must be specified by indicating the relative path from the "models" folder to the GraphML file, but without including the .graphml extension.
Example: if you would like to convert the ./models/example/example.graphml file, just provide example/example as an argument.

### Linux / *nix
Simply:

    ./porispanel.sh example/example

or, if wanting to sync it with a cosmoSys instance:

    ./porispanel_csys.sh example/example

The cosmoSys instance has to be configured by copying pyPORIS/config_rm_enabled.py.example to pyPORIS/config_rm_enabled.py and adding your secrets there.

If you have developed a model fragmented in several GraphML files (http://cosmobots.eu/projects/poris-toolkit/wiki/Fragmenting_diagrams), you can execute this conversion by calling the porispanel_dir.sh tool with the folder path.
For instance:

    ./porispanel_dir.sh osiris

The osiris example (inspired by the OSIRIS@GTC instrument at http://www.gtc.iac.es/instruments/osiris/) has been developed as a fragmented model.  One can explore the individual models as individual models.
For instance:

    ./porispanel.sh osiris/osiris
    ./porispanel.sh osiris/osidas
    ./porispanel.sh osiris/osifp
    ./porispanel.sh osiris/osifilt
    ./porispanel.sh osiris/osigeom

### Windows

POLICY: In cosmoBots.eu we are targeted to produce open source code for open source platforms.  Windows or Mac adaptations are never maintained by us.  They appear into our projects as external contributions, and we never check possible regressions after we update our tools.  Maintenance for those external contributions shall be external too.  Pull requests are welcome.

(so thanks Claudia)

Simply:

    winporispanel.bat example\example

or, if wanting to sync it with a cosmoSys instance:

    winporispanel_csys.bat example\example

The cosmoSys instance has to be configured by copying pyPORIS\config_rm_enabled.py.example to pyPORIS\config_rm_enabled.py and adding your secrets there.

The ability to convert a fragmented model is not yet available for Windows platforms (why not using a Linux or WSL or a docker container for this???).

## Generating Python PORIS classes from your models

Requirement: you must have generated an ODS file, check above.

### Linux / *nix
./redoPorisPython example/example

Simply:

    ./redoPorisPython.sh example/example

### Windows

Not yet implemented, but collaborations are welcome.  

POLICY: In cosmoBots.eu we are targeted to produce open source code for open source platforms.  Windows or Mac adaptations are never maintained by us.  They appear into our projects as external contributions, and we never check possible regressions after we update our tools.  Maintenance for those external contributions shall be external too.  Pull requests are welcome.

HINTS: Someone might want to adapt the redoPorisPython.sh to a redoPorisPython.bat, and doPorisPython.sh to doPorisPython.bat.
The generator is using symbolic links to allow the generated code to live in separate folders but being easy to test.  A similar behaviour should be created for windows.  
Easiest way is copying the PORIS/PORIS.py class and the automatically generated output/modename/modelname/modelnamePORIS.py class inside the output/modelname/modelname_physical/ folder, but having duplicated files is alwayas a bad idea. 
In order to have a repo which is easy to maintain, windows symbolic links solutions have to be analysed.

## Conclusion
Happy modeling!

cosmoBots.eu
