#!/bin/bash

DIR=$(realpath "$0" | xargs dirname)
PREFIX=/usr/bin

set -ex

for script in $(find "$DIR" -name 'htmlotate*' -maxdepth 1 -type f); do
    script_name=$(basename $script)
    ln -f -s "${script}" "$PREFIX/${script_name%.*}"
done
