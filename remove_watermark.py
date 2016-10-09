#!/usr/bin/python
import sys
import os.path

'''
    Author: Vivin Thomas Wilson
    version : 1.0
    python verson : Python 2.7.10 
    Description : Removes "Scanned by camscan" watermark from pdf 
'''

def usage():
    _WARN = '\033[91m'
    _END = '\033[0m'
    print ""
    print 'USAGE :'
    print _WARN+'python remove_watermark.py /path/to/file/file.pdf'+_END
    print 'replaces the old file with the modified file'
    print '(OR)'
    print _WARN+'python remove_watermark.py /path/to/file/file.pdf /path/to/modified/file/file.py'+_END
    print 'makes a new file with the changes'
    print ""
    exit(0)

def wmark_remove(from_file,to_file):
    f = open(from_file,'r')
    data = f.read().split("\n")
    f.close()

    f = open(to_file,"w")
    f.write("\n".join([i for i in data if not "(Scanned by CamScanner) Tj" in i]))
    f.close()

if __name__ == '__main__':

    to_file = ""
    from_file = ""

    if len(sys.argv) == 2:
       to_file = from_file = sys.argv[1]
    elif len(sys.argv) == 3:
       from_file = sys.argv[1]
       to_file = sys.argv[2]
    else:
       usage()
 
    wmark_remove(from_file,to_file)

