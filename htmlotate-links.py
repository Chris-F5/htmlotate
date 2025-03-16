#!/usr/bin/env python3

import sys
import re

for line in sys.stdin:
    line = line.strip('\n').strip('\r')
    line = re.sub(r'(https?://\S+)', r'<a href="\1">\1</a>', line)
    print(line)
