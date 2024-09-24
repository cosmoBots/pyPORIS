#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 1;
fi

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
echo "Script directory: $SCRIPT_DIR"

FILE=models/$1.graphml
FILE1=models/$1.ods
FILE3=models/$1.xml

if test -f "$FILE"; then
    echo "Input $FILE exists, continuing"
else
    echo "Input $FILE does not exist, aborting"
    exit 1;
fi

rm $FILE1
rm $FILE3

cp $SCRIPT_DIR/config_csys_disabled.py $SCRIPT_DIR/config_csys.py
python3 $SCRIPT_DIR/graph2poris.py $FILE || { echo "graph2poris could not be processed"; exit 1; }
if test -f "$FILE1"; then
    echo "Input $FILE1 exists, continuing"
else
    echo "Input $FILE1 does not exist, aborting"
    exit 1;
fi
python3 $SCRIPT_DIR/poris2xml.py $FILE1 || { echo "poris2xml could not be processed"; exit 1; } 
if test -f "$FILE3"; then
    echo "Input $FILE3 exists, continuing"
else
    echo "Input $FILE3 does not exist, aborting"
    exit 1;
fi
java -jar $SCRIPT_DIR/AstroPorisPlayer/bin/AstroPorisPlayer.jar $FILE3
