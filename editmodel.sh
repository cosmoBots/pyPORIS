##!/bin/bash
if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 1;
fi

FILE3=`pwd`/models/$1.graphml

if test -f "$FILE3"; then
    echo "Input $FILE3 exists, continuing"
else
    echo "Input $FILE3 does not exist, aborting"
    exit 1;
fi

if ! type yEd &> /dev/null; then
  yed $FILE3
else
  yEd $FILE3
fi
