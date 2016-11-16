#!/usr/bin/python
import sys
import os.path

'''
    Author: Vivin Thomas Wilson
    version : 1.2
    python verson : Python 2.7.10 
    Description : Removes "Scanned by camscan" watermark from pdf 
'''

def usage():
    _WARN = '\033[91m'
    _END = '\033[0m'
    print("")
    print('USAGE :')
    print(_WARN+'python remove_watermark.py /path/to/file/file.pdf'+_END)
    print('replaces the old file with the modified file')
    print('(OR)')
    print(_WARN+'python remove_watermark.py /path/to/file/file.pdf /path/to/modified/file/file.py'+_END)
    print('makes a new file with the changes')
    print("")
    exit(0)


def read_pdf_objects(input_file):
    f = open(input_file)
    data = f.read().split("\n")
    f.close()

    obj_store = {}
    read = False
    for i in data:
       if " obj" in i:
           read = True
           name = int(i.split()[0])
           tmp = ""

       if read:
           tmp += i+"\n"

       if "endobj" in i:
           read= False
           obj_store[name] = tmp
    return (obj_store,data)

def remove_watermark(obj_store):
    for key,value in obj_store.items():
        if "Scanned by CamScanner" in value:
            tmp_obj = value.split("\n")
            obj_store[key] = ""
            write = True
            omitted = 0
            for i in tmp_obj:
              if "BT" in i :
                  write = False
              if write:
                  obj_store[key] += i + "\n"
              else:
                 omitted += len(i) + 1
              if "ET" in i:
                  write = True
            len_obj_key = int(value.split("<<")[1].split(">>")[0].strip().split()[1])
            len_obj_val = obj_store[len_obj_key].split("\n")
            len_obj_val[1] = str(int(len_obj_val[1]) - omitted)
            obj_store[len_obj_key] =  "\n".join(len_obj_val)
    return obj_store

def write_file(data,obj_store,output_file):
    f = open(output_file,"w")
    write = True
    for i in data:
       if " obj" in i:
           write = False
           obj_key = int(i.split()[0])
       if write:
           f.write(i+"\n")
       if "endobj" in i:
           write = True
           f.write(obj_store[obj_key])
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
 
    obj_store,data = read_pdf_objects(from_file)
    obj_store = remove_watermark(obj_store)
    write_file(data,obj_store,to_file)
