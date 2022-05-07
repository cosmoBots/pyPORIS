#!/bin/bash
rm $1.ods
rm $1.xml
cp ../config_rm_enabled.py ../config_rm.py
python3 ../graph2poris.py $1.graphml
mv $1.graphml $1.old.graphml
mv $1.out.graphml $1.graphml
python3 ../poris2xml.py $1.ods
java -jar ../AstroPorisPlayer/bin/AstroPorisPlayer.jar $1.xml
