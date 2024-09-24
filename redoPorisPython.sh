#!/bin/bash

# Working directory clean
# Set the clean environment variable
export PORIS_CLEAN=1

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
echo "Script directory: $SCRIPT_DIR"

# Execute the doPorisPython.sh
$SCRIPT_DIR/doPorisPython.sh $1 || { echo 'doPorisPython.sh failed' ; exit 1; }
