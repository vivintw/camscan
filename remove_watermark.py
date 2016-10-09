#!/usr/bin/python
import sys

'''
    Author: Vivin Thomas Wilson
    version : 1.0
    python verson : Python 2.7.10 
    Description : Removes "Scanned by camscan" watermark from pdf 
'''

f = open(sys.argv[1])
data = f.read().split("\n")
f.close()
f = open(sys.argv[1],"w")
for i in data:
    if not "(Scanned by CamScanner) Tj" in i:
        f.write(i+"\n")
f.close()

