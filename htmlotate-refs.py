#!/usr/bin/env python3

import sys
import re

for line in sys.stdin:
    line = line.strip('\n').strip('\r')
    if match := re.search(r'^(\s*)\[([^\]]+)\](.*)$', line):
        leading_whitespace = match.group(1)
        ref = match.group(2)
        trailing_text = match.group(3)
        line = leading_whitespace \
             + f'<a id="#ref-{ref}">[{ref}]</a>' \
             + re.sub(r'\[([^\]]+)\]', r'<a href="#ref-\1">[\1]</a>', trailing_text)
    else:
        line = re.sub(r'\[([^\]]+)\]', r'<a href="#ref-\1">[\1]</a>', line)
    print(line)
