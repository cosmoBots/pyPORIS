# pyPORIS

A set of tools to manipulate PORIS instruments:

- porispanel.sh Creates a PORIS representation in ODS and XML format from a PORIS diagram in GraphML, and launches a configuration panel to validate the model.
- porispanel_csys.sh Adds to porispanel.sh the synchronization with a cosmoSys instance.
- porispanel_dir.sh Creates a PORIS representation in an ODS and XML format from a PORIS model which is fragmented in several GraphML files in the same folder.
- odsporispanel.sh Creates a PORIS representation in XML format and launches a configuration panel from an ODS file representing a PORIS model.
- porispanel_dir_csys.sh Adds to porispanel_dir.sh the synchronization with a cosmoSys instance.
- xmlporispanel.sh Launches a configuration panel from a PORIS model representation in XML file.
- redoPorisPython.sh and doPorisPython.sh converts an ODS representation of a PORIS model into convenient Python classes.
- runPorisModel.sh Generates the Python model with its physical companion if missing, and executes the physical model.

The models are taken from the ./models folder and the Python classes are generated inside ./output folder.

## Requirements

- Java (which can support Java Swing panels)
- Node.js and npm, for the optional Vue web viewer
- Python 3

Install python libraries:

- bs4 (< 4.13, because this version breaks the parser)
- lxml
- pyexcel_ods
- python-redmine

We have added requirements.txt and constraints.txt for taking care of the dependencies which could break the functionality.

If you want to install a venv with the strict requirements, you can do:

```
python -m venv venv
source venv/bin/activate
pip install --no-cache-dir -r requirements.txt
```

If you want to use newest pip libraries but respecting the constraints:

```
python -m venv venv
source venv/bin/activate
pip install -c constraints.txt bs4 lxml pyexcel_ods python-redmine
```

This is an example of how to install a valid Java platform in a modern Linux machine:

```
sudo apt install openjdk-17-jdk
```

If you want to use the Vue web viewer, install its dependencies once:

```
cd pyPORIS/porisViewer
npm ci
```

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

__Example__: if you would like to convert the ./models/example/example.graphml file, just provide example/example as an argument.

### Linux / *nix
For Bash model-path completion, source `scripts/poris-completion.bash` from
this toolkit (or `pyPORIS/scripts/poris-completion.bash` from the user repository).
Then `pyPORIS/porispanel.sh osi<Tab>` completes `osiris/`; further Tab presses
explore the models inside it, without the `.graphml` suffix. Completion uses
`models/` in the current working directory and also supports the `*_csys.sh`
and `porispanel_dir*.sh` variants. To load it persistently, add a `source`
command with the absolute script path to `~/.bashrc`.

Simply:

    ./porispanel.sh example/example

To open the generated XML with the Vue web viewer instead of the Java Swing
panel:

    ./porispanel.sh --web example/example

or, if wanting to sync it with a cosmoSys instance:

    ./porispanel_csys.sh <instance> example/example

Configure named connections in `csys.yaml` using `csys.yaml.example`. This file is ignored by Git. See the named-instance and remote-panel instructions below.

The synchronizer resolves items by their native cosmoSys CSID inside the configured root project tree. It creates missing items, then synchronizes their parent hierarchy, PORIS value metadata, and activation relations (`precedes`, delay `0`). The API user needs permission to read the project tree and create/edit the affected items and relations. This requires a cosmoSys version that provides the native item API used by the importer; it does not depend on legacy `csID`/`csCode` custom fields.

If you have developed a model fragmented in several GraphML files (http://cosmobots.eu/projects/poris-toolkit/wiki/Fragmenting_diagrams), you can execute this conversion by calling the porispanel_dir.sh tool with the folder path.
For instance:

    ./porispanel_dir.sh osiris

The directory and cosmoSys variants propagate the same viewer options:

    ./porispanel_dir.sh --web osiris
    ./porispanel_csys.sh <instance> --web example/example
    ./porispanel_dir_csys.sh <instance> --web osiris

Directory models can define their generated cluster name in
models/<model-dir>/cluster.yaml:

    cluster: osi
    root: osiris

If cluster.yaml is missing, porispanel_dir.sh stops and tells you how to create
the descriptor automatically:

    ./porispanel_dir.sh --cluster osi osiris

After that, ./porispanel_dir.sh osiris writes the composed Python product to
output/py/osiris/osiPORIS.py.

If cluster.yaml already exists, --cluster aborts; edit the descriptor or run
without --cluster.

The osiris example (inspired by the OSIRIS@GTC instrument at http://www.gtc.iac.es/instruments/osiris/) has been developed as a fragmented model.  One can explore the individual models as individual models.
For instance:

    ./porispanel.sh osiris/osiris
    ./porispanel.sh osiris/osidas
    ./porispanel.sh osiris/osifp
    ./porispanel.sh osiris/osifilt
    ./porispanel.sh osiris/osigeom

To open an existing XML with the web viewer:

    ./xmlporispanel.sh --web output/xml/osiris/osiris.xml

To generate XML from an ODS model and open it with the web viewer:

    ./odsporispanel.sh --web example/example

### Windows

__POLICY__: In cosmoBots.eu we are targeted to produce open source code for open source platforms.  Windows or Mac adaptations are never maintained by us.  They appear into our projects as external contributions, and we never check possible regressions after we update our tools.  Maintenance for those external contributions shall be external too.  Pull requests are welcome.

(so thanks Claudia)

Simply:

    winporispanel.bat example\example

For cosmoSys synchronization, use the named-instance shell commands above from
WSL. Connections are configured in `csys.yaml`; the old Python credential
configuration files have been removed.

The ability to convert a fragmented model is not yet available for Windows platforms (why not using a Linux or WSL or a docker container for this???).

## Generating Python PORIS classes from your models

Requirement: you must have generated an ODS file, check above.

### Linux / *nix

Simply:

    ./redoPorisPython.sh example/example

### Windows

Not yet implemented, but collaborations are welcome.  

__POLICY__: In cosmoBots.eu we are targeted to produce open source code for open source platforms.  Windows or Mac adaptations are never maintained by us.  They appear into our projects as external contributions, and we never check possible regressions after we update our tools.  Maintenance for those external contributions shall be external too.  Pull requests are welcome.

__HINTS__: Someone might want to adapt the redoPorisPython.sh to a redoPorisPython.bat, and doPorisPython.sh to doPorisPython.bat.
The generator is using symbolic links to allow the generated code to live in separate folders but being easy to test.  A similar behaviour should be created for windows.  

Easiest way is copying the PORIS/PORIS.py class and the automatically generated output/modename/modelname/modelnamePORIS.py class inside the output/modelname/modelname_physical/ folder, but having duplicated files is alwayas a bad idea.

In order to have a repo which is easy to maintain, windows symbolic links solutions have to be analysed.

## Conclusion
Happy modeling!

cosmoBots.eu

## Named cosmoSys Instances and Remote Panels

Install the requirements (including PyYAML), then copy `pyPORIS/csys.yaml.example`
to `pyPORIS/csys.yaml` and edit it. Paths here are relative to the user repository.
The real configuration is ignored by Git; do not put credentials in the example.

```yaml
cosmobots.eu:
  url: https://cosmobots.eu
  ignorecert: false
  key: "YOUR_API_KEY"
localhost:3001:
  url: http://localhost:3001
  ignorecert: false
  key: "YOUR_LOCAL_API_KEY"
```

URLs must include `http://` or `https://`. An empty key allows anonymous access.
Use `PORIS_CSYS_CONFIG=/absolute/path/csys.yaml` to select another configuration;
the remote viewer also accepts `--config PATH`.

Download and open a remote project or item:

```bash
pyPORIS/poriscsyspanel.sh localhost:3001 osiris
pyPORIS/poriscsyspanel.sh localhost:3001 osiris OSIRIS-0006
pyPORIS/poriscsyspanel.sh localhost:3001 osiris 22202
pyPORIS/poriscsyspanel.sh http://localhost:3001/projects/osiris/poris
pyPORIS/poriscsyspanel.sh http://localhost:3001/issues/22202
pyPORIS/poriscsyspanel.sh --web --scope node localhost:3001 osiris 22202
```

The command name is `poriscsyspanel.sh` in both argument forms. URL input selects
credentials by matching the configured server URL (including an installation
subpath); unknown or ambiguous instances are rejected. Query-string `scope` and
`issue_id` are supported on project/PORIS URLs. `--scope` overrides the URL scope.
Credentials in pasted URLs are not used. Redirects are not followed.

Scopes match the server viewer:

- `project`: project and its visible subprojects; default for project input.
- `node_down`: item and descendants; default for item input, including item URLs.
- `node`: the server's focused node view.

CSIDs and numeric issue IDs are resolved through the native item API. For an
item URL, the standard Redmine issue API supplies its project. Both require the
corresponding read permissions. The XML endpoint must support API authentication.
An item in a child project is opened using that item's own project.

The default viewer is Java Swing; `--web` opens the local web viewer. For Java, downloaded
XML is ordered with destinations before their referring elements and the system
root last, as required by the Java loader. IDs and model relationships are preserved. With `--web`, the original XML is
validated and passed unchanged to porisViewer, without reordering. The command
only reads cosmoSys and does not synchronize edits or preserve server UI sessions.
XML is temporary unless `--output FILE` is supplied. Download without launching:

```bash
pyPORIS/poriscsyspanel.sh --no-panel --output /tmp/osiris.xml localhost:3001 osiris
```

Local GraphML synchronization uses the same named configuration:

```bash
pyPORIS/porispanel_csys.sh localhost:3001 --no-panel nrt/mainaxis
pyPORIS/porispanel_dir_csys.sh localhost:3001 --no-panel osiris
# Equivalent direct form:
pyPORIS/porispanel.sh --csys localhost:3001 --no-panel nrt/mainaxis
```

The old Python credential files are not read by these commands. Synchronization
writes to cosmoSys, unlike the remote-panel command. When calling Python importers
directly, set `PORIS_CSYS_INSTANCE` to the configured instance name.

## Shared Python Output Directory

Python products mirror the source directory, without per-model wrapper folders.
For `models/osiris/osiris.graphml` and the `cluster: osi` descriptor in
`models/osiris/cluster.yaml`, the products coexist:

```text
output/py/osiris/osirisPORIS.py
output/py/osiris/osiPORIS.py
```

Regenerating a model replaces only its own generated Python file. Other models
and editable physical companions are preserved. Physical companions live in
`output/py/<source-directory>/<model>_physical/`. GraphML panel commands, the
ODS panel command and the Python generation/run shell commands use this layout.
