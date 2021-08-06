def isprime(n):
    for i in range(2,n):
        if n%i!=0:
            continue
        else:
            return False
    return True

n = int(input("Enter a limit:"))
for i in range(2,n+1):
    if isprime(i)==True:
        print(i)
    else:
        continue






