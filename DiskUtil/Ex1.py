import os
import sys
import time

def diskspace(dir):
    disksize=0
    for root,dirs,files in os.walk(dir):
        for names in files:
            path=os.path.abspath(os.path.join(root,names))
            disksize=disksize+os.stat(path).st_size
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
            print(filename,"\t\t\t",path,"\t\t\t",ByteToMb(size),"M","\t\t\t",times)


def checkoption(arg):
    checkpoint =1
    for choices in arg :
        if checkpoint == 1:
            checkpoint+=1
            continue
        else:
            if(choices== "-h" or choices== "-help"):
                print("Available Help Options")
                print("-c - Current Directory")
                print("-p - Parent Directory")
                print(" Or  can pass absolute bath as a command line argument")
            elif(choices== "-c"):
                print("Current Directory Details")
                listfun(".")
            elif(choices== "-p"):
                print("Parent Directory Details")
                listfun("..")
            else:
                listfun(choices)
            

def main():
    if(len(sys.argv)>0 and len(sys.argv)==1):
        print("Pass -h or -help as Command line argument for help")
    else:
                checkoption(sys.argv)

main()