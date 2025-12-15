##!/bin/bash
if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 1;
fi

DIR=models/$1
FILE1=models/$1/$1.ods
FILE3=models/$1/$1.xml

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PYTHON_BIN="${SCRIPT_DIR}/../.venv/bin/python"
if [ ! -x "$PYTHON_BIN" ]; then
  PYTHON_BIN="python3"
fi
echo "Script directory: $SCRIPT_DIR"

if test -d "$DIR"; then
    echo "Input $DIR exists, continuing"
else
    echo "Input $DIR does not exist, aborting"
    exit 1;
fi

rm -f $FILE1
rm -f $FILE3

cp $SCRIPT_DIR/config_csys_disabled.py $SCRIPT_DIR/config_csys.py
$PYTHON_BIN $SCRIPT_DIR/graphdir2poris.py $DIR || { echo "graph2poris could not be processed"; exit 1; }
if test -f "$FILE1"; then
    echo "Input $FILE1 exists, continuing"
else
    echo "Input $FILE1 does not exist, aborting"
    exit 1;
fi
$PYTHON_BIN $SCRIPT_DIR/poris2xml.py $FILE1 || { echo "poris2xml could not be processed"; exit 1; } 
if test -f "$FILE3"; then
    echo "Input $FILE3 exists, continuing"
else
    echo "Input $FILE3 does not exist, aborting"
    exit 1;
fi
# Only launch the viewer when a display is available (avoid headless errors)
if [ -n "$DISPLAY" ]; then
    java -jar $SCRIPT_DIR/AstroPorisPlayer/bin/AstroPorisPlayer.jar $FILE3
else
    echo "DISPLAY is not set; skipping AstroPorisPlayer launch for $FILE3"
fi
