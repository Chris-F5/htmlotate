#!/usr/bin/bash

if [ -z "$1" ]; then
    echo "Usage: htmlotate <file or directory>"
    exit 1
fi

for f in $(find $1 -type f -executable -name '*.htmlotate'); do
    echo "${f%.htmlotate}.html"
    $(realpath "$f") > ${f%.htmlotate}.html
done
