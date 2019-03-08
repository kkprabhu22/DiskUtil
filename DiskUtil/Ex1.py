import os

def listfun(dir):
    for root,dirs,files in os.walk(dir):
        for names in files:
            filename=names
            path=os.path.abspath(os.path.join(root,names))

            print(filename,"\t\t\t\t\t\t",path)

def main():
    print("Select the options")
    print("1-Show current Directory Details")
    print("2-Show Parent Directory Details")
    dir=input()
    if(dir =="1"):
        listfun(".")
    elif(dir =="2"):
        listfun("..")
    else:
        print("Invalid Option")

main()
