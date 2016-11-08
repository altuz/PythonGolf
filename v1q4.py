#!/usr/local/bin/python3.5
import sys, re;
[ print(re.sub(r"(\d+(\.\d+)+)", lambda x: str(int(round(float(x.group(0))))) if re.match(r'^(\d+(\.\d+){0,1})$', x.group(0)) else x.group(0), line.rstrip())) for line in sys.stdin ]
#for all lines in standard in, replaces floats with its rounded value
#ignores non floats like '3.' or 127.0.0.1
#anon = lambda x,y=0: x+y
#print(anon(3, 4))
