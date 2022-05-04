#!/bin/bash

python3 graph2poris.py ./example.graphml
python3 poris2xml.py ./example.ods
java -jar AstroPorisPlayer/bin/AstroPorisPlayer.jar ./example.xml
