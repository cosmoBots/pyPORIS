# Importing auxiliar libraries for the test
import argparse  # This library allows us to easily parse the command line arguments
import os
from pathlib import Path

from pyexcel_ods import get_data  # This function allows us to easily read an ODS file (for api)

# Importing test configuration file
import config
from poris_codegen import build_nodes_tree, createPythonCode


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


parser = argparse.ArgumentParser(description='Launches a PORIS device generation from an ODS file describing the PORIS instrument')
parser.add_argument('model_root_path', type=dir_path, help="the root path where the models shall be picket from")
parser.add_argument('model_path', type=argparse.FileType('r'), help="the path for the model to be processed")
parser.add_argument('output_path', type=dir_path, help="the path to create the Python classes")

args = parser.parse_args()

print("/* The PORIS instrument description ODS filename is:", args.model_path.name + " */")
deviceName = Path(args.model_path.name).stem
print("Device name:", deviceName)

relativepath = args.model_path.name.replace(args.model_root_path, '', 1)
relativepath = ''.join(relativepath.rsplit(".ods", 1))

print(config.welcome_message)


def loadODS():
    dictdata = get_data(args.model_path.name, start_row=config.dict_max_rows_row, row_limit=config.dict_max_rows_row + 1,
        start_column=config.dict_max_rows_column, column_limit=config.dict_max_rows_column)[config.dict_file_sheet]

    desc_file_row_limit = dictdata[0][1]
    filedata = get_data(args.model_path.name, start_row=config.desc_file_start_row, row_limit=desc_file_row_limit,
        start_column=config.desc_file_start_column, column_limit=config.desc_file_column_limit)
    nodesdata = filedata[config.desc_file_sheet]

    virtual_nodes_counter = 1
    nodes_dict = {}
    rowcount = 0

    for row in nodesdata:
        if len(row) > 1:
            rowcount += 1
            thiskey = row[config.desc_ident_column]
            if len(thiskey) > 0:
                thisnode = {}
                thisnode['ident'] = thiskey
                thisid = str(row[config.desc_id_column])
                if len(thisid) <= 0:
                    thisid = 2000000000 + rowcount

                thisnode['id'] = thisid
                thisnode['subject'] = row[config.desc_subject_column]
                thisnode['description'] = row[config.desc_description_column]
                thisnode['parent'] = row[config.desc_parent_column]
                blockingstr = row[config.desc_blocking_column]
                thisnode['tracker'] = row[config.desc_tracker_column]
                thisnode['blocking'] = []
                thisnode['virtual'] = False
                if blockingstr is not None and len(blockingstr) > 0:
                    thisnode['blocking'] = [x.strip() for x in blockingstr.split(',')]
                else:
                    if thisnode['tracker'] == "prMode":
                        virtnode = {}
                        virtid = str(-virtual_nodes_counter)
                        virtual_nodes_counter += 1
                        virtident = "VIRT" + virtid
                        virtnode['ident'] = virtident
                        virtnode['id'] = virtid
                        virtnode['tracker'] = "prValue"
                        virtnode['subject'] = thisnode['subject']
                        virtnode['description'] = thisnode['description']
                        virtnode['parent'] = thisnode['parent']
                        virtnode['blocking'] = []
                        virtnode['precedents'] = []
                        virtnode['children'] = []
                        virtnode['virtual'] = True
                        nodes_dict[virtident] = virtnode
                        thisnode['blocking'] = [virtident]
                    else:
                        thisnode['blocking'] = []

                thisnode['min'] = row[config.desc_min_column]
                thisnode['default_data'] = row[config.desc_def_column]
                thisnode['max'] = row[config.desc_max_column]
                thisnode['deftext'] = row[config.desc_deftext_column]
                precedentstr = row[config.desc_precedents_column]
                thisnode['precedents'] = []
                if precedentstr is not None:
                    thisnode['precedents'] = [x.strip() for x in precedentstr.split(',')]
                else:
                    thisnode['precedents'] = []

                thisnode['children'] = []
                nodes_dict[thiskey] = thisnode

    return build_nodes_tree(nodes_dict, config.savemem)


nodes_dict = loadODS()
createPythonCode(nodes_dict, deviceName, args.output_path, relativepath)
