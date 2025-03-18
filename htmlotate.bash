#!/usr/bin/bash

if [ -z "$1" ]; then
    echo "Usage: htmlotate <file or directory>"
    exit 1
fi

for f in $(find $1 -type f -executable -name '*.htmlotate'); do
    echo "HTMLOTATE ${f%.htmlotate}.html"
    f_abs=$(realpath "$f")
    (cd $(dirname "$f") && $f_abs > ${f_abs%.htmlotate}.html)
done
