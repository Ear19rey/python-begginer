def total():
    num = input("enter a number:")
    if num =='':
        return 0
    else:

        return float(num)+total()

def main():
    print("The total is",total())

if __name__=='__main__':
    main()