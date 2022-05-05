#!/bin/bash
python3 ../graph2poris.py $1.graphml
python3 ../poris2xml.py $1.ods
java -jar ../AstroPorisPlayer/bin/AstroPorisPlayer.jar $1.xml
