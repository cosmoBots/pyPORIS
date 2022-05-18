#!/bin/bash
rm models/$1.ods
rm models/$1.xml
cp config_rm_enabled.py config_rm.py || { echo "config_rm_enabled.py missing"; exit 1; } 
python3 graph2poris.py models/$1.graphml || { echo "graph2poris could not be processed"; exit 1; }
timestamp=$(date +%s)
cp models/$1.graphml models/$1.$timestamp.backup
mv models/$1.graphml models/$1.old.graphml
mv models/$1.out.graphml models/$1.graphml
python3 poris2xml.py models/$1.ods || { echo "poris2xml could not be processed"; exit 1; } 
java -jar AstroPorisPlayer/bin/AstroPorisPlayer.jar models/$1.xml

