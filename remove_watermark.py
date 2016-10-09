#!/usr/bin/python
import sys

f = open(sys.argv[1])
data = f.read().split("\n")
f.close()
f = open(sys.argv[1],"w")
for i in data:
    if not "(Scanned by CamScanner) Tj" in i:
        f.write(i+"\n")
f.close()

