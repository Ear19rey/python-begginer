def pdm(n):
    if len(n)>0 and n[0]==n[-1]:
        n = n[1:-1]
        return pdm(n)
    elif len(n)==0:
        return "It's Palindrome!"
    else:
        return "It's not Palindrome!"

def main():
    n = input("Enter a word to check whether Palindrome or not:")
    print(pdm(n))

if __name__=="__main__":
    main()
