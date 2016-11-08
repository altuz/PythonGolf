#!/usr/local/bin/python3.5
import re, sys, fileinput
lines = [ line.rstrip() for line in sys.stdin ]
print('\n'.join(map(lambda x: re.sub(r'^#(\d+)$', lambda y: lines[int(y.group(1))], x), lines)))
