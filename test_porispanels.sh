#!/bin/bash

set -euo pipefail

WITH_CSYS=0
PROMPT_BEFORE=1
NO_DIR=0
EXTRA_ARGS=()

usage() {
    echo "Usage: $0 [--with-csys] [--no-prompt] [--nodir] [--ods] [--parser-xml] [--web] [--no-panel]"
    echo
    echo "Sequentially launches PORIS panels for the models under models/."
    echo "Close each AstroPorisPlayer window to continue with the next case."
    echo "--nodir treats every GraphML file as an individual model and skips directory-model generation."
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --with-csys)
            WITH_CSYS=1
            shift
            ;;
        --no-prompt)
            PROMPT_BEFORE=0
            shift
            ;;
        --nodir)
            NO_DIR=1
            shift
            ;;
        --ods|--parser-xml|--compare-parser|--web|--no-panel)
            EXTRA_ARGS+=("$1")
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

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
REPO_ROOT="$( cd "${SCRIPT_DIR}/.." &> /dev/null && pwd )"

cd "$REPO_ROOT"

mapfile -t GRAPH_MODELS < <(
    find models -type f -name '*.graphml' \
        | sed 's#^models/##; s#\.graphml$##' \
        | sort
)
DIR_MODELS=()
if [ $NO_DIR -eq 0 ] && [ -d "models/osiris" ]; then
    DIR_MODELS+=("osiris")
fi

TOTAL=${#GRAPH_MODELS[@]}
TOTAL=$((TOTAL + ${#DIR_MODELS[@]}))
if [ $WITH_CSYS -eq 1 ]; then
    TOTAL=$((TOTAL * 2))
fi
CURRENT=0

run_case() {
    local script_name="$1"
    local model_name="$2"
    shift 2
    local args=("$@")

    CURRENT=$((CURRENT + 1))
    echo
    echo "[$CURRENT/$TOTAL] ${script_name} ${args[*]} ${model_name}"
    if [ $PROMPT_BEFORE -eq 1 ]; then
        read -r -p "Press Enter to launch this panel..."
    fi
    if ! "${SCRIPT_DIR}/${script_name}" "${args[@]}" "$model_name"; then
        if [ $NO_DIR -eq 1 ]; then
            echo "Skipped failed individual model: ${model_name}"
            return 0
        fi
        return 1
    fi
}

echo "Visual PORIS panel validation"
echo "GraphML models: ${#GRAPH_MODELS[@]}"
echo "Directory models: ${#DIR_MODELS[@]}"
if [ $NO_DIR -eq 1 ]; then
    echo "Directory-model generation disabled by --nodir."
fi
if [ ${#EXTRA_ARGS[@]} -gt 0 ]; then
    echo "Extra porispanel arguments: ${EXTRA_ARGS[*]}"
fi
if [ $WITH_CSYS -eq 0 ]; then
    echo "CSYS variants are skipped. Use --with-csys to include porispanel_csys.sh and porispanel_dir_csys.sh."
fi

for model in "${GRAPH_MODELS[@]}"; do
    run_case "porispanel.sh" "$model" "${EXTRA_ARGS[@]}"
done

for model in "${DIR_MODELS[@]}"; do
    run_case "porispanel_dir.sh" "$model" "${EXTRA_ARGS[@]}"
done

if [ $WITH_CSYS -eq 1 ]; then
    for model in "${GRAPH_MODELS[@]}"; do
        run_case "porispanel_csys.sh" "$model" "${EXTRA_ARGS[@]}"
    done

    for model in "${DIR_MODELS[@]}"; do
        run_case "porispanel_dir_csys.sh" "$model" "${EXTRA_ARGS[@]}"
    done
fi

echo
echo "Visual validation run completed."
