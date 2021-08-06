n = int(input("Enter an integer!:"))
factor =2
if  n >=2:
    while True:
        if n%factor==0:
            n=n/factor
            print(factor)
        else:
            factor +=1    
else:
     print("integer has to be bigger than 2!!!")

