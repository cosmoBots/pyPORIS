#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 1;
fi

FILE=models/$1.graphml
if test -f "$FILE"; then
    echo "Input $FILE exists, continuing"
else
    echo "Input $FILE does not exist, aborting"
    exit 1;
fi

rm models/$1.ods
rm models/$1.xml
cp config_rm_disabled.py config_rm.py
python3 graph2poris.py $FILE || { echo "graph2poris could not be processed"; exit 1; } 
python3 poris2xml.py models/$1.ods || { echo "poris2xml could not be processed"; exit 1; } 
java -jar AstroPorisPlayer/bin/AstroPorisPlayer.jar models/$1.xml
