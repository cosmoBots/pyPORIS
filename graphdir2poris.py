# Note, thanks to https://github.com/viperior/graphml-interpreter
import argparse
from locale import normalize                     # This library allows us to easily parse the command line arguments
import pathlib

from graphdir2porisprocess import *

######### WE WILL PARSE THE COMMAND LINE ARGUMENTS FOR THE WRAPPER GEN #############
parser = argparse.ArgumentParser(description='Launches a PORIS device generation ODS from an GraphML diagrams directory describing the PORIS instrument')

## The second argument is the api ODS file
parser.add_argument('sys_dir',type=pathlib.Path, help="the path of a directory containing the PORIS instrument diagram")

# Obtaining the arguments from the command line
args=parser.parse_args()

# Printing the obtained arguments:
print("/* The PORIS instrument diagram directory is:",args.sys_dir.name+" */")
deviceName = pathlib.Path(args.sys_dir.name).stem
print("Device name:",deviceName)

# As an example of a constant defined in the configuration file, we'll print the welcome message
print(config.welcome_message)

create_tree_from_graphml_dir('models/'+args.sys_dir.name,deviceName)
