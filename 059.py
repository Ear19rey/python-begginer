n = str(input("Enter your license(ABC123 or 1234ABC):"))
if len(n)==6:
    a=n[0:3]
    b=n[3:6]
    if not a.isalpha() or not b.isdigit():
        print("Invalid")
    else:
        if a.isupper():
            print("Valid")
        else:
            print("Invalid")
elif len(n)==7:
    c=n[0:4]
    d=n[4:7]
    if not c.isdigit() or not d.isalpha():
        print("Invalid")
    else:
        if d.isupper():
            print("Valid")
        else:
            print("Invalid")
else:
    print("wrong input")