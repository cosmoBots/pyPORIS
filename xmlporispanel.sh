#!/bin/bash

LAUNCH_WEB=0

usage() {
    echo "Usage: $0 [--web] <model-path-without-extension-or-xml-file>"
}

while [[ "$1" == --* ]]; do
    case "$1" in
        --web)
            LAUNCH_WEB=1
            shift
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            usage
            exit 1
            ;;
    esac
done

if [ $# -eq 0 ]; then
    echo "No arguments supplied"
    usage
    exit 1
fi

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
SCRIPTS_DIR="${SCRIPT_DIR}/scripts"
echo "Script directory: $SCRIPT_DIR"

DEVPATH="$1"
if test -f "$DEVPATH"; then
    FILE3="$DEVPATH"
elif [[ "$DEVPATH" == *.xml ]]; then
    FILE3="$DEVPATH"
else
    FILE3="models/${DEVPATH}.xml"
fi

if test -f "$FILE3"; then
    echo "Input $FILE3 exists, continuing"
else
    echo "Input $FILE3 does not exist, aborting"
    exit 1;
fi

if [ $LAUNCH_WEB -eq 1 ]; then
    "$SCRIPTS_DIR/launch_poris_webviewer.sh" "$FILE3" "$DEVPATH"
else
    java -jar "$SCRIPT_DIR/AstroPorisPlayer/bin/AstroPorisPlayer.jar" "$FILE3"
fi
