#!/bin/bash

if [ $# -eq 0 ]; then
  echo "Usage: $0 <model-path-without-extension>"
  echo "Example: $0 nrt/mainaxis"
  exit 1
fi

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
MODEL_PATH="$1"
MODEL_NAME="${MODEL_PATH##*/}"
OUTPUT_BASE_DIR="$(pwd)/output/py/${MODEL_NAME}"
OUTPUT_MODEL_DIR="${OUTPUT_BASE_DIR}/${MODEL_NAME}"
OUTPUT_PHYS_DIR="${OUTPUT_BASE_DIR}/${MODEL_NAME}_physical"
export PYTHONPATH="${SCRIPT_DIR}/PORIS:${OUTPUT_MODEL_DIR}:${PYTHONPATH}"

DO_PORIS_ARGS=("${MODEL_PATH}")
if [ -d "models/${MODEL_PATH}" ]; then
  DO_PORIS_ARGS=(--dir "${MODEL_PATH}")
fi

if [ ! -d "${OUTPUT_MODEL_DIR}" ] || [ ! -f "${OUTPUT_MODEL_DIR}/${MODEL_NAME}PORIS.py" ]; then
  echo "Python model not found in output, generating with doPorisPython.sh"
  PORIS_SAFETY_OVERRIDE=1 "${SCRIPT_DIR}/doPorisPython.sh" "${DO_PORIS_ARGS[@]}" || { echo "doPorisPython.sh failed" ; exit 1; }
fi

if [ ! -d "${OUTPUT_PHYS_DIR}" ] || [ ! -f "${OUTPUT_PHYS_DIR}/${MODEL_NAME}_physical.py" ]; then
  echo "Physical companion not found in output, generating with doPorisPython.sh"
  PORIS_SAFETY_OVERRIDE=1 "${SCRIPT_DIR}/doPorisPython.sh" "${DO_PORIS_ARGS[@]}" || { echo "doPorisPython.sh failed" ; exit 1; }
fi

cd "${OUTPUT_PHYS_DIR}"
if [ ! -f "${MODEL_NAME}_physical.py" ]; then
  echo "Error: physical model file not found: ${MODEL_NAME}_physical.py"
  exit 1
fi

python3 "${MODEL_NAME}_physical.py"
