def dtb(a):
    if a==0:
        return "0"
    elif a==1:
        return "1"
    else:
        c = str(a%2)
        return dtb(a//2)+c

def main():
    a = int(input("Enter an integer:"))
    print(a,"changed to be",dtb(a))

if __name__=="__main__":
    main()