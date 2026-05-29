#!/bin/bash

GENERATE_PARSER_XML=0
LAUNCH_PANEL=1

while [[ "$1" == --* ]]; do
  case "$1" in
    --parser-xml|--compare-parser)
      GENERATE_PARSER_XML=1
      shift
      ;;
    --no-panel)
      LAUNCH_PANEL=0
      shift
      ;;
    *)
      echo "Unknown option: $1"
      echo "Usage: $0 [--parser-xml] [--no-panel] <model-path-without-extension>"
      exit 1
      ;;
  esac
done

if [ $# -eq 0 ]; then
  echo "No arguments supplied"
  echo "Usage: $0 [--parser-xml] [--no-panel] <model-path-without-extension>"
  exit 1
fi

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
DEVPATH="$1"
DEVNAME="${DEVPATH##*/}"
DEVDIR="$(dirname "${DEVPATH}")"
if [ "${DEVDIR}" = "." ]; then
  DEVDIR=""
fi

INPUT_ODS="models/${DEVPATH}.ods"
MODEL_ROOT="models"
if [ -n "${DEVDIR}" ]; then
  MODEL_ROOT="models/${DEVDIR}"
fi

OUTPUT_BASE_DIR="$(pwd)/output/py/${DEVNAME}"
OUTPUT_PORIS_DIR="${OUTPUT_BASE_DIR}/${DEVNAME}"
OUTPUT_MODEL_FILE="${OUTPUT_PORIS_DIR}/${DEVNAME}PORIS.py"
OUTPUT_XML_DIR="$(pwd)/output/xml/${DEVDIR}"
OUTPUT_XML_FILE="${OUTPUT_XML_DIR}/${DEVNAME}.xml"
PARSER_XML_FILE="${OUTPUT_XML_DIR}/${DEVNAME}.from-parser.xml"
OUTPUT_XML_DIFF="${OUTPUT_XML_DIR}/${DEVNAME}.xml.diff"

export PYTHONPATH="${SCRIPT_DIR}/PORIS:${OUTPUT_PORIS_DIR}:${PYTHONPATH}"

if test -f "$INPUT_ODS"; then
  echo "Input $INPUT_ODS exists, continuing"
else
  echo "Input $INPUT_ODS does not exist, aborting"
  exit 1
fi

rm -rf "$OUTPUT_PORIS_DIR"
rm -f "$OUTPUT_XML_FILE" "$PARSER_XML_FILE" "$OUTPUT_XML_DIFF"
mkdir -p "$OUTPUT_PORIS_DIR" "$OUTPUT_XML_DIR"

python3 "$SCRIPT_DIR/poris2python.py" "$MODEL_ROOT" "$INPUT_ODS" "$OUTPUT_BASE_DIR" || { echo "poris2python could not be processed"; exit 1; }
if test -f "$OUTPUT_MODEL_FILE"; then
  echo "Generated Python model $OUTPUT_MODEL_FILE exists, continuing"
else
  echo "Generated Python model $OUTPUT_MODEL_FILE does not exist, aborting"
  exit 1
fi

if [ $GENERATE_PARSER_XML -eq 1 ]; then
  python3 "$SCRIPT_DIR/poris2xml.py" "$INPUT_ODS" --output-dir "$OUTPUT_XML_DIR" || { echo "poris2xml could not be processed"; exit 1; }
  if test -f "$OUTPUT_XML_FILE"; then
    mv "$OUTPUT_XML_FILE" "$PARSER_XML_FILE"
  else
    echo "Parser-generated XML $OUTPUT_XML_FILE does not exist, aborting"
    exit 1
  fi
fi

python3 "$SCRIPT_DIR/poris_python2xml.py" "$OUTPUT_MODEL_FILE" --output "$OUTPUT_XML_FILE" || { echo "poris_python2xml could not be processed"; exit 1; }
if test -f "$OUTPUT_XML_FILE"; then
  echo "Python XML: $OUTPUT_XML_FILE"
else
  echo "Python-generated XML $OUTPUT_XML_FILE does not exist, aborting"
  exit 1
fi

if [ $GENERATE_PARSER_XML -eq 1 ]; then
  echo "Parser XML: $PARSER_XML_FILE"
  if diff -u "$PARSER_XML_FILE" "$OUTPUT_XML_FILE" > "$OUTPUT_XML_DIFF"; then
    echo "XML files are equal"
    rm -f "$OUTPUT_XML_DIFF"
  else
    echo "XML files differ; diff written to $OUTPUT_XML_DIFF"
  fi
fi

if [ $LAUNCH_PANEL -eq 1 ]; then
  java -jar "$SCRIPT_DIR/AstroPorisPlayer/bin/AstroPorisPlayer.jar" "$OUTPUT_XML_FILE"
else
  echo "Skipping AstroPorisPlayer launch for $OUTPUT_XML_FILE"
fi
