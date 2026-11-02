#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
exec python3 "$SCRIPT_DIR/scripts/csys_panel.py" "$@"
