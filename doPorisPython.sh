#!/bin/bash

if [ $# -eq 0 ]; then
  echo "No arguments supplied"
  exit 1;
fi

DIRMODE=0
GENERATE_ODS=0

# Parse optional flags
while [[ "$1" == --* ]]; do
  case "$1" in
    --dir)
      DIRMODE=1
      shift
      ;;
    --ods)
      GENERATE_ODS=1
      shift
      ;;
    *)
      echo "Unknown option: $1"
      exit 1
      ;;
  esac
done

if [ -z "$1" ]; then
  echo "No device name supplied"
  exit 1
fi

if [ $DIRMODE -eq 1 ]; then
  FILE=models/$1
  if [ -d "$FILE" ]; then
      echo "Input dir $FILE exists, continuing"
  else
      echo "Input dir $FILE does not exist, aborting"
      exit 1;
  fi
else
  FILE=models/$1.graphml
  if test -f "$FILE"; then
      echo "Input $FILE exists, continuing"
  else
      echo "Input $FILE does not exist, aborting"
      exit 1;
  fi
fi

if [ -z ${PORIS_SAFETY_OVERRIDE+x} ]; then 
    echo "PORIS_SAFETY_OVERRIDE is not set, checking repo is clean";
    if [ -z "$(git status --porcelain)" ]; then 
        echo "Welcome to doPorisPython.sh"
    else 
        # Uncommitted changes
        echo "ERROR: YOUR REPOSITORY IS NOT CLEAN"
        echo "As executing this process can overwrite manual code"
        echo "you are encouraged to have commited/reverted any change"
        echo "in the repo so in case of loosing something you will have"
        echo "the opportunity to recover it (in case you commited it)"
        echo "or you will be the only responsible of having lost it "
        echo "(in case you reverted)."
        exit 1;
    fi
else
    echo "PORIS_SAFETY_OVERRIDE is set, skip checking repo is clean";
    echo "Welcome to doPorisPython.sh"
fi

######### SAFETY AREA ############


########### USER CONFIGURATION AREA ##############

# Defining some environmental variables
# TODO: Convert them to arguments
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
DEVBASE_PATH=`pwd`

########### INTERNAL VARIABLES CALCULATION AREA ##############

# Some "constants"
# The name of the device, get from the script first argument
DEVPATH=$1
DEVNAME=${DEVPATH##*/}
OUTPUT_BASE=${DEVPATH%"$DEVNAME"}
echo ${DEVPATH}
echo ${DEVNAME}
echo ${OUTPUT_BASE}
OUTPUT_BASE_DIR=${DEVBASE_PATH}/output/py/${DEVNAME}
OUTPUT_PORIS_DIR=${OUTPUT_BASE_DIR}/${DEVNAME}

# The path for the C++ base folder for the devices


# This is the folder for the PORIS tools path.
# Normally set to PORIS_TOOLS_PYTHON_PATH=${DEVBASE_PYTHON_PATH}/PORIS, but if you
# change DEVBASE_RELATIVE_PATH you might want to separate the link
# between the two variables
PORIS_TOOLS_PATH=${SCRIPT_DIR}
PORIS_TOOLS_PYTHON_PATH=${SCRIPT_DIR}
echo "path"
echo ${PORIS_TOOLS_PATH}
echo ${PORIS_TOOLS_PYTHON_PATH}

# The path for the C++ base folder for the specific (user) custom code of the device
OUTPUT_PHYS_PATH=${OUTPUT_BASE_DIR}/${DEVNAME}_physical

########### WELCOME MESSAGE CALCULATION AREA ##############

echo "Welcome to Python code generator por PORIS models"

######### CLEANING AREA ###############
# We will clean the previous products
echo "Cleaning previous generated products"
rm -rf ${OUTPUT_BASE_DIR}

######### CREATING FOLDERS AREA ###############
# Let's create the product directories
echo "Creating ${OUTPUT_PORIS_DIR}"
mkdir -p ${OUTPUT_PORIS_DIR}
ln -s ../../../../pyPORIS/PORIS/PORIS.py ${OUTPUT_PORIS_DIR}/PORIS.py

######### If no USER CUSTOM CODE FOLDER ADDED, COPY THE TEMPLATE ONE #############
echo "Checking the existence of ${OUTPUT_PHYS_PATH}"
if [ -d "$OUTPUT_PHYS_PATH" ]; then
  ### Take action if $DEVBASE_PHYS_PATH exists ###
  echo "${OUTPUT_PHYS_PATH} already present, nothing to do"
else
  ###  Control will jump here if $DEVBASE_PYTHON_PHYS_PATH does NOT exists ###
  echo "${OUTPUT_PHYS_PATH} not found. Copying template dir."
  cp -r ${PORIS_TOOLS_PYTHON_PATH}'/PORIS/$S1_physical' ${OUTPUT_PHYS_PATH}
  echo ${DEVNAME}
  echo "Renaming"${OUTPUT_PHYS_PATH}'/$S1_physical.py to '${OUTPUT_PHYS_PATH}/${DEVNAME}_physical.py
  mv ${OUTPUT_PHYS_PATH}'/$S1_physical.py' ${OUTPUT_PHYS_PATH}/${DEVNAME}_physical.py
  sed -i "s/DEVICENAME/$DEVNAME/" ${OUTPUT_PHYS_PATH}/${DEVNAME}_physical.py
  sed -i "s/DEVICENAME/$DEVNAME/" ${OUTPUT_PHYS_PATH}/${DEVNAME}_physical.py
  sed -i "s/DEVICENAME/$DEVNAME/" ${OUTPUT_PHYS_PATH}/${DEVNAME}_physical.py
  sed -i "s/DEVICENAME/$DEVNAME/" ${OUTPUT_PHYS_PATH}/${DEVNAME}_physical.py
  ln -s ../${DEVNAME}/${DEVNAME}PORIS.py ${OUTPUT_PHYS_PATH}/${DEVNAME}PORIS.py
  ln -s ../../../../pyPORIS/PORIS/PORIS.py ${OUTPUT_PHYS_PATH}/PORIS.py
fi

######### PARSING THE MODEL AND GENERATING THE PORIS PRODUCTS ###############
cd ${DEVBASE_PATH}
echo "Generating the PORIS device products from $1.graphml"
echo ${PORIS_TOOLS_PYTHON_PATH}
ODS_FLAG="--no-ods"
if [ $GENERATE_ODS -eq 1 ]; then
  ODS_FLAG=""
fi
if [ $DIRMODE -eq 1 ]; then
  python3 ${PORIS_TOOLS_PYTHON_PATH}/graphdir2poris.py $ODS_FLAG --output-dir ${OUTPUT_PORIS_DIR} models/$1 || { echo 'graphdir2poris.py failed' ; exit 1; }
else
  python3 ${PORIS_TOOLS_PYTHON_PATH}/graph2poris.py $ODS_FLAG models/$1.graphml --output-dir ${OUTPUT_PORIS_DIR} || { echo 'graph2poris.py failed' ; exit 1; }
fi

echo "Fin!"
