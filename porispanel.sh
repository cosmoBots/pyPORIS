#!/bin/bash

GENERATE_PARSER_XML=0
GENERATE_ODS=0
DIRMODE=0
CSYS_MODE=0
LAUNCH_PANEL=1
LAUNCH_WEB=0
DEBUG_JSON=0
CLUSTER_NAME_ARG=""

usage() {
    echo "Usage: $0 [--dir] [--csys] [--ods] [--parser-xml] [--debug] [--web] [--no-panel] [--cluster <name>] <model-path-without-extension>"
}

while [[ "$1" == --* ]]; do
    case "$1" in
        --dir)
            DIRMODE=1
            shift
            ;;
        --csys)
            CSYS_MODE=1
            shift
            ;;
        --no-panel)
            LAUNCH_PANEL=0
            shift
            ;;
        --web)
            LAUNCH_WEB=1
            shift
            ;;
        --ods)
            GENERATE_ODS=1
            shift
            ;;
        --parser-xml|--compare-parser)
            GENERATE_PARSER_XML=1
            shift
            ;;
        --debug)
            DEBUG_JSON=1
            shift
            ;;
        --cluster)
            if [ $# -lt 2 ]; then
                echo "--cluster requires a cluster name"
                usage
                exit 1
            fi
            CLUSTER_NAME_ARG="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            usage
            exit 1
            ;;
    esac
done

if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    usage
    exit 1;
fi

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
SCRIPTS_DIR="${SCRIPT_DIR}/scripts"
echo "Script directory: $SCRIPT_DIR"

DEVPATH=$1
INPUT_DEVNAME=${DEVPATH##*/}
DEVNAME=${INPUT_DEVNAME}
DEVDIR=$(dirname "${DEVPATH}")
if [ "${DEVDIR}" = "." ]; then
    DEVDIR=""
fi
if [ $DIRMODE -eq 1 ]; then
    FILE=models/$1
    DEVDIR=$(dirname "${DEVPATH}")
    if [ "${DEVDIR}" = "." ]; then
        DEVDIR=""
    fi
elif [ -d "models/$1" ]; then
    DIRMODE=1
    FILE=models/$1
    DEVDIR=$(dirname "${DEVPATH}")
    if [ "${DEVDIR}" = "." ]; then
        DEVDIR=""
    fi
else
    FILE=models/$1.graphml
fi

read_cluster_yaml_key() {
    local file="$1"
    local key="$2"
    sed -nE "s/^[[:space:]]*${key}[[:space:]]*:[[:space:]]*['\"]?([^'\"#]+)['\"]?.*$/\1/p" "$file" | head -n 1 | sed -E 's/[[:space:]]+$//'
}

validate_python_name() {
    local value="$1"
    local label="$2"
    if [[ ! "$value" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
        echo "$label '$value' is not a valid Python identifier"
        exit 1
    fi
}

CLUSTER_ROOT_NAME="$INPUT_DEVNAME"
GRAPH_DIR_ARGS=()
CLUSTER_DIR_OUTPUT=0
if [ $DIRMODE -eq 1 ]; then
    CLUSTER_FILE="${FILE}/cluster.yaml"
    if [ ! -d "$FILE" ]; then
        echo "Input $FILE does not exist, aborting"
        exit 1
    fi
    if [ -n "$CLUSTER_NAME_ARG" ]; then
        validate_python_name "$CLUSTER_NAME_ARG" "Cluster name"
        if [ -f "$CLUSTER_FILE" ]; then
            echo "$CLUSTER_FILE already exists."
            echo "Edit that file or run without --cluster."
            exit 1
        fi
        {
            echo "cluster: ${CLUSTER_NAME_ARG}"
            echo "root: ${INPUT_DEVNAME}"
        } > "$CLUSTER_FILE"
        echo "Created $CLUSTER_FILE"
    fi

    if [ -f "$CLUSTER_FILE" ]; then
        CLUSTER_NAME=$(read_cluster_yaml_key "$CLUSTER_FILE" "cluster")
        CLUSTER_ROOT_NAME=$(read_cluster_yaml_key "$CLUSTER_FILE" "root")
        if [ -z "$CLUSTER_NAME" ]; then
            echo "$CLUSTER_FILE must define a non-empty 'cluster' value"
            exit 1
        fi
        validate_python_name "$CLUSTER_NAME" "Cluster name"
        if [ -z "$CLUSTER_ROOT_NAME" ]; then
            echo "$CLUSTER_FILE must define a non-empty 'root' value"
            exit 1
        fi
        DEVNAME="$CLUSTER_NAME"
        CLUSTER_DIR_OUTPUT=1
        GRAPH_DIR_ARGS=(--device-name "$CLUSTER_NAME" --root "$CLUSTER_ROOT_NAME")
        echo "Cluster descriptor: $CLUSTER_FILE"
        echo "Cluster product name: $DEVNAME"
        echo "Cluster root graph: $CLUSTER_ROOT_NAME"
        if [ ! -f "${FILE}/${CLUSTER_ROOT_NAME}.graphml" ]; then
            echo "Cluster root graph ${FILE}/${CLUSTER_ROOT_NAME}.graphml does not exist, aborting"
            exit 1
        fi
    else
        echo "$CLUSTER_FILE does not exist."
        echo "Directory models require a cluster descriptor."
        echo "To create a cluster descriptor, run:"
        echo "  pyPORIS/porispanel_dir.sh --cluster <cluster-name> $DEVPATH"
        exit 1
    fi
elif [ -n "$CLUSTER_NAME_ARG" ]; then
    echo "--cluster can only be used with directory models"
    exit 1
fi

if [ $DIRMODE -eq 1 ] && [ $CLUSTER_DIR_OUTPUT -eq 1 ]; then
    OUTPUT_BASE_DIR="$(pwd)/output/py/${DEVPATH}/${DEVNAME}"
    OUTPUT_PORIS_DIR="${OUTPUT_BASE_DIR}"
else
    OUTPUT_BASE_DIR="$(pwd)/output/py/${DEVDIR}/${DEVNAME}"
    OUTPUT_PORIS_DIR="${OUTPUT_BASE_DIR}/${DEVNAME}"
fi
OUTPUT_MODEL_FILE="${OUTPUT_PORIS_DIR}/${DEVNAME}PORIS.py"
if [ $DIRMODE -eq 1 ] && [ $CLUSTER_DIR_OUTPUT -eq 1 ]; then
    OUTPUT_ODS_DIR="$(pwd)/output/ods/${DEVPATH}"
    OUTPUT_XML_DIR="$(pwd)/output/xml/${DEVPATH}"
else
    OUTPUT_ODS_DIR="$(pwd)/output/ods/${DEVDIR}"
    OUTPUT_XML_DIR="$(pwd)/output/xml/${DEVDIR}"
fi
FILE1="${OUTPUT_ODS_DIR}/${DEVNAME}.ods"
OUTPUT_XML_FILE="${OUTPUT_XML_DIR}/${DEVNAME}.xml"
PARSER_XML_FILE="${OUTPUT_XML_DIR}/${DEVNAME}.from-parser.xml"
OUTPUT_XML_DIFF="${OUTPUT_XML_DIR}/${DEVNAME}.xml.diff"
export PYTHONPATH="${SCRIPT_DIR}/PORIS:${OUTPUT_PORIS_DIR}:${PYTHONPATH}"

if [ $DIRMODE -eq 1 ] && test -d "$FILE"; then
    echo "Input $FILE exists, continuing"
elif [ $DIRMODE -eq 0 ] && test -f "$FILE"; then
    echo "Input $FILE exists, continuing"
else
    echo "Input $FILE does not exist, aborting"
    exit 1;
fi
if [ $GENERATE_PARSER_XML -eq 1 ] && [ $GENERATE_ODS -eq 0 ]; then
    echo "--parser-xml requires --ods because parser XML is generated from the ODS product"
    exit 1
fi

if [ $GENERATE_ODS -eq 1 ]; then
    rm -f "$FILE1"
fi
rm -f "$OUTPUT_XML_FILE"
rm -f "$PARSER_XML_FILE"
rm -f "${OUTPUT_XML_DIR}/${DEVNAME}.from-python.xml"
rm -f "$OUTPUT_XML_DIFF"
if [ $DIRMODE -eq 1 ] && [ $CLUSTER_DIR_OUTPUT -eq 1 ]; then
    rm -f "$OUTPUT_MODEL_FILE"
else
    rm -rf "${OUTPUT_PORIS_DIR}"
fi
mkdir -p "${OUTPUT_PORIS_DIR}"
if [ $GENERATE_ODS -eq 1 ]; then
    mkdir -p "${OUTPUT_ODS_DIR}"
fi
mkdir -p "${OUTPUT_XML_DIR}"

if [ $CSYS_MODE -eq 1 ]; then
    cp "$SCRIPTS_DIR/config_csys_enabled.py" "$SCRIPTS_DIR/config_csys.py" || { echo "$SCRIPTS_DIR/config_csys_enabled.py missing"; exit 1; }
else
    cp "$SCRIPTS_DIR/config_csys_disabled.py" "$SCRIPTS_DIR/config_csys.py"
fi
ODS_ARGS=(--no-ods)
if [ $GENERATE_ODS -eq 1 ]; then
    ODS_ARGS=(--ods-output-dir "${OUTPUT_ODS_DIR}")
fi
DEBUG_ARGS=()
if [ $DEBUG_JSON -eq 1 ]; then
    DEBUG_ARGS=(--debug)
fi
if [ $DIRMODE -eq 1 ]; then
    python3 "$SCRIPTS_DIR/graphdir2poris.py" --output-dir "${OUTPUT_PORIS_DIR}" "${ODS_ARGS[@]}" "${DEBUG_ARGS[@]}" "${GRAPH_DIR_ARGS[@]}" "$FILE" || { echo "graphdir2poris could not be processed"; exit 1; }
else
    python3 "$SCRIPTS_DIR/graph2poris.py" "$FILE" --output-dir "${OUTPUT_PORIS_DIR}" "${ODS_ARGS[@]}" || { echo "graph2poris could not be processed"; exit 1; }
    FILE2="${FILE}.out"
    if [ $CSYS_MODE -eq 1 ]; then
        if test -f "$FILE2"; then
            echo "Input $FILE2 exists, continuing"
        else
            echo "Input $FILE2 does not exist, aborting"
            exit 1;
        fi
        timestamp=$(date +%s)
        cp "$FILE" "${FILE}.${timestamp}.backup"
        mv "$FILE" "${FILE}.old"
        mv "$FILE2" "$FILE"
    fi
fi
if test -f "$OUTPUT_MODEL_FILE"; then
    echo "Generated Python model $OUTPUT_MODEL_FILE exists, continuing"
else
    echo "Generated Python model $OUTPUT_MODEL_FILE does not exist, aborting"
    exit 1;
fi
if [ $GENERATE_ODS -eq 1 ]; then
    if test -f "$FILE1"; then
        echo "Generated ODS $FILE1 exists, continuing"
    else
        echo "Generated ODS $FILE1 does not exist, aborting"
        exit 1;
    fi
fi

if [ $GENERATE_PARSER_XML -eq 1 ]; then
    python3 "$SCRIPTS_DIR/poris2xml.py" "$FILE1" --output-dir "${OUTPUT_XML_DIR}" || { echo "poris2xml could not be processed"; exit 1; } 
    if test -f "$OUTPUT_XML_FILE"; then
        mv "$OUTPUT_XML_FILE" "$PARSER_XML_FILE"
        echo "Parser-generated XML $PARSER_XML_FILE exists, continuing"
    else
        echo "Parser-generated XML $OUTPUT_XML_FILE does not exist, aborting"
        exit 1;
    fi
fi
python3 "$SCRIPTS_DIR/poris_python2xml.py" "$OUTPUT_MODEL_FILE" --output "$OUTPUT_XML_FILE" || { echo "poris_python2xml could not be processed"; exit 1; }
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
if [ $LAUNCH_PANEL -eq 1 ]; then
    if [ $LAUNCH_WEB -eq 1 ]; then
        "$SCRIPTS_DIR/launch_poris_webviewer.sh" "$OUTPUT_XML_FILE" "$DEVPATH"
    else
        java -jar $SCRIPT_DIR/AstroPorisPlayer/bin/AstroPorisPlayer.jar $OUTPUT_XML_FILE
    fi
else
    echo "Skipping PORIS panel launch for $OUTPUT_XML_FILE"
fi
