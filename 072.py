n = str(input("Enter a word:"))
a=n
while True:
    if len(a)>0 and a[0]==a[-1]:
        a = a[1:-1]
        print(a)
    elif len(a)==0:
        print(n,"is a Palindrome!")
        break
    else:
        print(n,"is not a Palindrome!")
        break