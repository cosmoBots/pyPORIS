##!/bin/bash
if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 1;
fi

FILE3=models/$1.xml

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
echo "Script directory: $SCRIPT_DIR"

if test -f "$FILE3"; then
    echo "Input $FILE3 exists, continuing"
else
    echo "Input $FILE3 does not exist, aborting"
    exit 1;
fi
java -jar $SCRIPT_DIR/AstroPorisPlayer/bin/AstroPorisPlayer.jar $FILE3
