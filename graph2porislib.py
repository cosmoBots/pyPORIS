# Note, thanks to https://github.com/viperior/graphml-interpreter
import argparse                     # This library allows us to easily parse the command line arguments

import csv, os, re
from bs4 import BeautifulSoup
from pyexcel_ods import save_data
from collections import OrderedDict
from pathlib import Path
from config_rm import *

# Importing test configuration file
import config

def convert_list_to_string(list, delimiter):
  list_string = ''

  if len(list)>0:
    for item in list[:-1]:
      list_string = list_string + item + delimiter

    list_string = list_string + list[-1]

  return list_string

def convert_sorted_list_to_dictionary_with_sequence_index(list):
  dictionary_with_sequence_index = {}

  for index, value in enumerate(list):
    dictionary_with_sequence_index[value] = index + 1

  return dictionary_with_sequence_index

