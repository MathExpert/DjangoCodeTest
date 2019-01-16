#!/bin/bash

# Snippet for script directory taken from "https://stackoverflow.com/questions/59895/getting-the-source-directory-of-a-bash-script-from-within"
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

source "${SCRIPT_DIR}"/config.sh

docker run -it --rm -p ${EXPOSE_PORT}:${EXPOSE_PORT} \
           --name "${CONTAINER_NAME}" \
           -v $(pwd)/cloud_test_app:/opt/cloud_test_app \
           "${IMAGE_NAME}" \
           "$@"
