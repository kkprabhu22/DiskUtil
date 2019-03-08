import os

def listfun(dir):
    filenames=os.listdir(dir)
    print("File name\t File path\t\t\t\t\tFile Size")

    for filename in filenames:
        if(os.path.isdir(filename)):
            folder=os.listdir(filename)
            for files in folder:
                path=os.path.abspath(os.path.join(dir,filename))
                size=os.stat(filename)
                print(files,"\t",path,"\t\t",size.st_size)
        else:
            path=os.path.abspath(os.path.join(dir,filename))
            size=os.stat(filename)
            print(filename,"\t",path,"\t\t",size.st_size)

def main():
    print("Select the options")
    print("1-Show current directory Details")
    print("2-Show Parent Directory Details")
    dir=input()
    if(dir =="1"):
        listfun(".")
    elif(dir =="2"):
        listfun("..")
    else:
        print("Invalid Option")

main()
