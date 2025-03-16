#!/usr/bin/env python3

import sys
import re

for line in sys.stdin:
    line = line.strip('\n').strip('\r')
    line = re.sub(r'[^^]\[(.+)\]', r'<a href="#ref-\1">[\1]</a>', line)
    line = re.sub(r'^\[(.+)\]', r'<a id="ref-\1">[\1]</a>', line)
    print(line)
