def gcd(a,b):
    if b == 0:
        return a
    else:
        c=a%b
        return gcd(b,c)

def main():
    a = int(input("Enter a integer:"))
    b = int(input("Enter a integer:"))
    print(gcd(a,b))

if __name__=="__main__":
    main()