import sys
def head(n):
    with open(n,'r',encoding='utf-8') as f:
        a = f.readlines()
        for i in range(10):
            print(a[i].replace('\n',''))
if len(sys.argv)!=2:
    print("Provide a filename!")
    quit()
try:
    head(sys.argv[1])
except IOError:
    print("An error occurred while accessing the file!!!")
