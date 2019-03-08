import os
import sys
import time

def listfun(dir):
    for root,dirs,files in os.walk(dir):
        for names in files:
            filename=names
            path=os.path.abspath(os.path.join(root,names))
            size=os.stat(path).st_size
            times=time.ctime(os.path.getmtime(path))
            print("Filename -  ",filename)
            print("File Absolute path -  ",path)
            print("File Size in Bytes -  ",size)
            print("File last Modification time -  ",times)
            print("*******************************************************************************************")
def main():
    while True:
         print("Select the options")
         print("1-Show current Directory Details")
         print("2-Show Parent Directory Details")
         dir=input()
         if(dir =="1"):
             listfun(".")
         elif(dir =="2"):
             listfun("..")
        #  elif(dir =="3"):
        #      listfun(dir)
        #      print("working oncode part")
         else:
             sys.exit(0)

main()
