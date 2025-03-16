#!/bin/bash

DIR=$(realpath "$0" | xargs dirname)
PREFIX=/usr/bin

set -ex

ln -f -s "$DIR/htmlotate.bash" "$PREFIX/htmlotate"

for script in $(find "$DIR" -name '*.py' -maxdepth 1 -type f); do
    script_name=$(basename $script)
    ln -f -s "${script}" "$PREFIX/${script_name%.py}"
done
