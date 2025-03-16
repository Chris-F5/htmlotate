#!/usr/bin/env python3

import html
import sys

for line in sys.stdin:
    line = line.rstrip('\n').rstrip('\r')
    print(html.escape(line))
