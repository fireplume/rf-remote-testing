#!/bin/bash

if [[ $# != 1 ]]; then
    echo "Usage: $0 target_lib_path"
    echo "__init__.py needs to be configured with the remote target library install path."
    echo "That is the absolute path where 'server.py' and libraries are found."
    exit 0
fi

target_lib_path=$1

sed -i -e "s#REMOTE_PROJECT_PATH_TAG#$1#" host/__init__.robot

echo "Please inspect host/__init__.robot to make sure REMOTE_ROOT_PROJECT is set properly."
