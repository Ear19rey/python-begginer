x = int(input("Enter an integer:"))
guess = x/2
print(guess)
while True:
    a = str(input("Good or not? Enter y or n:"))
    if a == "n":
        guess = (guess + x/guess)/2
        print(guess)
    else:
        if a == "y":
            print("The square root of",x,"is",guess)
            break
