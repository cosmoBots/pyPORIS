#!/bin/bash
rm $1.ods
rm $1.xml
cp ../config_rm_disabled.py ../config_rm.py
python3 ../graph2poris.py $1.graphml || { echo "graph2poris could not be processed"; exit 1; } 
python3 ../poris2xml.py $1.ods || { echo "poris2xml could not be processed"; exit 1; } 
java -jar ../AstroPorisPlayer/bin/AstroPorisPlayer.jar $1.xml
