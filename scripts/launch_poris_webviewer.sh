#!/bin/bash

set -euo pipefail

if [ $# -lt 1 ]; then
    echo "Usage: $0 <xml-file> [model-name]"
    exit 1
fi

XML_FILE=$1
MODEL_NAME=${2:-$(basename "$XML_FILE" .xml)}
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PYPORIS_DIR="$( cd "${SCRIPT_DIR}/.." &> /dev/null && pwd )"
VIEWER_DIR="${PYPORIS_DIR}/porisViewer"
PUBLIC_DIR="${VIEWER_DIR}/public"
RUNTIME_DIR="${PUBLIC_DIR}/runtime"
PORT="${PORIS_WEB_PORT:-5173}"
HOST="${PORIS_WEB_HOST:-127.0.0.1}"
LOG_FILE="${VIEWER_DIR}/porisviewer-vite.log"

if [ ! -f "$XML_FILE" ]; then
    echo "Generated XML file $XML_FILE does not exist, aborting"
    exit 1
fi

if ! command -v node >/dev/null 2>&1; then
    echo "Node.js is required to run the PORIS web viewer."
    echo "Install Node.js and npm, then run:"
    echo "  cd $VIEWER_DIR"
    echo "  npm ci"
    exit 1
fi

if ! command -v npm >/dev/null 2>&1; then
    echo "npm is required to run the PORIS web viewer."
    echo "Install npm, then run:"
    echo "  cd $VIEWER_DIR"
    echo "  npm ci"
    exit 1
fi

if [ ! -d "${VIEWER_DIR}/node_modules" ]; then
    echo "PORIS web viewer dependencies are not installed."
    echo "Run:"
    echo "  cd $VIEWER_DIR"
    if [ -f "${VIEWER_DIR}/package-lock.json" ]; then
        echo "  npm ci"
    else
        echo "  npm install"
    fi
    exit 1
fi

mkdir -p "$RUNTIME_DIR"
MODEL_STEM="${MODEL_NAME%.xml}"
SAFE_MODEL_NAME=$(printf '%s' "$MODEL_STEM" | tr '/ ' '__')
RUNTIME_FILE="${RUNTIME_DIR}/${SAFE_MODEL_NAME}.xml"
cp "$XML_FILE" "$RUNTIME_FILE"
MODEL_PATH="/runtime/${SAFE_MODEL_NAME}.xml"
ENCODED_MODEL_PATH=$(node -e "console.log(encodeURIComponent(process.argv[1]))" "$MODEL_PATH")
URL="http://${HOST}:${PORT}/?model=${ENCODED_MODEL_PATH}"

server_is_up() {
    if command -v curl >/dev/null 2>&1; then
        curl -fsS "http://${HOST}:${PORT}/" >/dev/null 2>&1
    else
        return 1
    fi
}

if server_is_up; then
    echo "Using existing PORIS web viewer at http://${HOST}:${PORT}/"
else
    echo "Starting PORIS web viewer on http://${HOST}:${PORT}/"
    (
        cd "$VIEWER_DIR"
        nohup npm run dev -- --host "$HOST" --port "$PORT" --strictPort > "$LOG_FILE" 2>&1 &
    )

    if command -v curl >/dev/null 2>&1; then
        for _ in $(seq 1 30); do
            if server_is_up; then
                break
            fi
            sleep 1
        done
        if ! server_is_up; then
            echo "The PORIS web viewer did not start on http://${HOST}:${PORT}/"
            echo "Check the log at $LOG_FILE"
            exit 1
        fi
    else
        sleep 3
    fi
fi

echo "PORIS web viewer URL:"
echo "$URL"

if [ "${PORIS_WEB_NO_OPEN:-0}" = "1" ]; then
    exit 0
fi

if command -v xdg-open >/dev/null 2>&1; then
    xdg-open "$URL" >/dev/null 2>&1 &
elif command -v open >/dev/null 2>&1; then
    open "$URL" >/dev/null 2>&1 &
elif [ -n "${BROWSER:-}" ]; then
    "$BROWSER" "$URL" >/dev/null 2>&1 &
else
    echo "No browser opener was found. Open the URL above manually."
fi
