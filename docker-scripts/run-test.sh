#!/bin/bash

# Snippet for script directory taken from "https://stackoverflow.com/questions/59895/getting-the-source-directory-of-a-bash-script-from-within"
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

source "${SCRIPT_DIR}"/config.sh

source "${SCRIPT_DIR}/build-image.sh"
source "${SCRIPT_DIR}/run-default.sh"
