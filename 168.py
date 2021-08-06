def sqrt(n,guess=1.0):
    if abs(n-guess**2) <=n*(10**-12):
        return guess
    else:
        guess = (guess+n/guess)/2
        return sqrt(n,guess)

def main():
    n = float(input("Enter a number:"))
    print(sqrt(n))

if __name__=="__main__":
    main()