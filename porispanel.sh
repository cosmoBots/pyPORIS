#!/bin/bash

GENERATE_PARSER_XML=0

while [[ "$1" == --* ]]; do
    case "$1" in
        --parser-xml|--compare-parser)
            GENERATE_PARSER_XML=1
            shift
            ;;
        *)
            echo "Unknown option: $1"
            echo "Usage: $0 [--parser-xml] <model-path-without-extension>"
            exit 1
            ;;
    esac
done

if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    echo "Usage: $0 [--parser-xml] <model-path-without-extension>"
    exit 1;
fi

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
echo "Script directory: $SCRIPT_DIR"

FILE=models/$1.graphml
DEVPATH=$1
DEVNAME=${DEVPATH##*/}
DEVDIR=$(dirname "${DEVPATH}")
if [ "${DEVDIR}" = "." ]; then
    DEVDIR=""
fi
OUTPUT_BASE_DIR="$(pwd)/output/py/${DEVNAME}"
OUTPUT_PORIS_DIR="${OUTPUT_BASE_DIR}/${DEVNAME}"
OUTPUT_MODEL_FILE="${OUTPUT_PORIS_DIR}/${DEVNAME}PORIS.py"
OUTPUT_ODS_DIR="$(pwd)/output/ods/${DEVDIR}"
OUTPUT_XML_DIR="$(pwd)/output/xml/${DEVDIR}"
FILE1="${OUTPUT_ODS_DIR}/${DEVNAME}.ods"
OUTPUT_XML_FILE="${OUTPUT_XML_DIR}/${DEVNAME}.xml"
PARSER_XML_FILE="${OUTPUT_XML_DIR}/${DEVNAME}.from-parser.xml"
OUTPUT_XML_DIFF="${OUTPUT_XML_DIR}/${DEVNAME}.xml.diff"
export PYTHONPATH="${SCRIPT_DIR}/PORIS:${OUTPUT_PORIS_DIR}:${PYTHONPATH}"

if test -f "$FILE"; then
    echo "Input $FILE exists, continuing"
else
    echo "Input $FILE does not exist, aborting"
    exit 1;
fi

rm -f "$FILE1"
rm -f "$OUTPUT_XML_FILE"
rm -f "$PARSER_XML_FILE"
rm -f "${OUTPUT_XML_DIR}/${DEVNAME}.from-python.xml"
rm -f "$OUTPUT_XML_DIFF"
rm -rf "${OUTPUT_PORIS_DIR}"
mkdir -p "${OUTPUT_PORIS_DIR}"
mkdir -p "${OUTPUT_ODS_DIR}"
mkdir -p "${OUTPUT_XML_DIR}"

cp $SCRIPT_DIR/config_csys_disabled.py $SCRIPT_DIR/config_csys.py
python3 $SCRIPT_DIR/graph2poris.py $FILE --output-dir "${OUTPUT_PORIS_DIR}" --ods-output-dir "${OUTPUT_ODS_DIR}" || { echo "graph2poris could not be processed"; exit 1; }
if test -f "$OUTPUT_MODEL_FILE"; then
    echo "Generated Python model $OUTPUT_MODEL_FILE exists, continuing"
else
    echo "Generated Python model $OUTPUT_MODEL_FILE does not exist, aborting"
    exit 1;
fi
if test -f "$FILE1"; then
    echo "Input $FILE1 exists, continuing"
else
    echo "Input $FILE1 does not exist, aborting"
    exit 1;
fi

if [ $GENERATE_PARSER_XML -eq 1 ]; then
    python3 $SCRIPT_DIR/poris2xml.py "$FILE1" --output-dir "${OUTPUT_XML_DIR}" || { echo "poris2xml could not be processed"; exit 1; } 
    if test -f "$OUTPUT_XML_FILE"; then
        mv "$OUTPUT_XML_FILE" "$PARSER_XML_FILE"
        echo "Parser-generated XML $PARSER_XML_FILE exists, continuing"
    else
        echo "Parser-generated XML $OUTPUT_XML_FILE does not exist, aborting"
        exit 1;
    fi
fi
python3 $SCRIPT_DIR/poris_python2xml.py "$OUTPUT_MODEL_FILE" --output "$OUTPUT_XML_FILE" || { echo "poris_python2xml could not be processed"; exit 1; }
if test -f "$OUTPUT_XML_FILE"; then
    echo "Python-generated XML $OUTPUT_XML_FILE exists, continuing"
else
    echo "Python-generated XML $OUTPUT_XML_FILE does not exist, aborting"
    exit 1;
fi
echo "Python XML: $OUTPUT_XML_FILE"
if [ $GENERATE_PARSER_XML -eq 1 ]; then
    echo "Parser XML: $PARSER_XML_FILE"
    if diff -u "$PARSER_XML_FILE" "$OUTPUT_XML_FILE" > "$OUTPUT_XML_DIFF"; then
        echo "XML files are equal"
        rm -f "$OUTPUT_XML_DIFF"
    else
        echo "XML files differ; diff written to $OUTPUT_XML_DIFF"
    fi
fi
java -jar $SCRIPT_DIR/AstroPorisPlayer/bin/AstroPorisPlayer.jar $OUTPUT_XML_FILE
