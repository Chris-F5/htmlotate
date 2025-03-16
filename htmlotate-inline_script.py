#!/usr/bin/env python3

import sys
import subprocess
import argparse

def run_shell(command, input=""):
    result = subprocess.run(command, shell=True, input=input,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    sys.stderr.write(result.stderr)
    sys.stdout.write(result.stdout)
    if result.returncode != 0:
        exit(1)

parser = argparse.ArgumentParser()
parser.add_argument('filename', nargs='?', default=None)
args = parser.parse_args()

FILE = open(args.filename) if args.filename else sys.stdin

mode = "verbatim"
command = None
payload = ""

try:
    for line in FILE:
        if len(line) > 0 and line[0] == '#':
            continue
        if mode == "verbatim":
            parts = line.strip().split(" ", 1)
            if parts[0] == "!BEGIN":
                command = parts[1]
                mode = "command"
            elif parts[0] == "!EXEC":
                run_shell(parts[1])
            else:
                sys.stdout.write(line)
        elif mode == "command":
            if line.strip() == "!END":
                run_shell(command, payload)
                mode = "verbatim"
                command = None
                payload = ""
            else:
                payload += line
    FILE.close()
except KeyboardInterrupt:
    print()
    exit(130)
