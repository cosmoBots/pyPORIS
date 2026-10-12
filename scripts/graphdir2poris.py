# Note, thanks to https://github.com/viperior/graphml-interpreter
import argparse
from locale import normalize                     # This library allows us to easily parse the command line arguments
import pathlib

from graphdir2porisprocess import *

######### WE WILL PARSE THE COMMAND LINE ARGUMENTS FOR THE WRAPPER GEN #############
parser = argparse.ArgumentParser(description='Launches a PORIS device generation from a GraphML diagrams directory describing the PORIS instrument')

## The second argument is the api ODS file
parser.add_argument('sys_dir',type=pathlib.Path, help="the path of a directory containing the PORIS instrument diagram")
parser.add_argument('--no-ods', action='store_true', help="skip ODS generation")
parser.add_argument('--debug', action='store_true', help="write intermediate debug JSON files under tmp/poris-debug")
parser.add_argument('--output-dir', help="directory where the generated Python file will be stored (defaults to the GraphML folder)")
parser.add_argument('--ods-output-dir', help="directory where the generated ODS file will be stored (defaults to the GraphML folder)")
parser.add_argument('--device-name', help="name of the generated PORIS Python/XML product (defaults to the directory name)")
parser.add_argument('--root', help="GraphML file stem that acts as the cluster root (defaults to the device name)")

# Obtaining the arguments from the command line
args=parser.parse_args()

# Printing the obtained arguments:
graph_dir = args.sys_dir
if not graph_dir.exists():
    graph_dir = pathlib.Path('models') / args.sys_dir

print("/* The PORIS instrument diagram directory is:",str(graph_dir)+" */")
deviceName = args.device_name or pathlib.Path(graph_dir.name).stem
rootName = args.root or deviceName
print("Device name:",deviceName)
print("Root graph:",rootName)

# As an example of a constant defined in the configuration file, we'll print the welcome message
print(config.welcome_message)

create_tree_from_graphml_dir(
    str(graph_dir),
    deviceName,
    emit_ods=not args.no_ods,
    emit_python=True,
    python_output_dir=args.output_dir,
    ods_output_dir=args.ods_output_dir,
    root_name=rootName,
    debug_json=args.debug,
)
