import os
import sys
import time

def diskspace(dir):
    disksize=0
    for root,dirs,files in os.walk(dir):
        for names in files:
            path=os.path.abspath(os.path.join(root,names))
            disksize=disksize+os.stat(path).st_size
    print("*******************************************************************************************")
    print("Directory size in Bytes- ",ByteToMb(disksize),"M")
    print("*******************************************************************************************")

def ByteToMb(size):
    size=format(size/1000000,".4f")
    return size


def listfun(dir):
    diskspace(dir)
    for root,dirs,files in os.walk(dir):
        for names in files:
            filename=names
            path=os.path.abspath(os.path.join(root,names))
            size=os.stat(path).st_size
            times=time.ctime(os.path.getmtime(path))
            print("Filename -  ",filename)
            print("File Absolute path -  ",path)
            print("File Size in Bytes -  ",ByteToMb(size),"M")
            print("File last Modification time -  ",times)
            print("*******************************************************************************************")
def main():
    while True:
         print("Select the options")
         print("1-Show Current Directory Details")
         print("2-Show Parent Directory Details")
         print("3- Specific Directory Details ")
         dir=input()
         if(dir =="1"):
             listfun(".")
         elif(dir =="2"):
             listfun("..")
         elif(dir =="3"):
             print("Input Absolute path of the directory in the following format ----C:/Users/admin/Downloads")
             dirpath=input()
             listfun(dirpath)
         else:
             sys.exit(0)

main()