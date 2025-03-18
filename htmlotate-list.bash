#!/bin/bash

header="Type  Date        Size  Name"
format="%y\t%TF\t%s\t%f\n"

(find .. -maxdepth 0 -printf $format ;  find . -maxdepth 1 ! -name ".*" -printf $format) \
  | sort -t$'\t' -k1,1 -k4,4  \
  | numfmt --delimiter=$'\t' --field=3 --to=iec \
  | awk -F'\t' '{$4="<a href=\"./" $4 "\">" $4 "</a>"; print}' OFS="\t" \
  | awk -F'\t' '{printf "%-5s %-11s %-5s %s\n", $1, $2, $3, $4}' \
  | sed "1i $header"
