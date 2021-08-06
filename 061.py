a= float(input())
sum = 0
ct = 1
if a ==0:
    print("Error")
else:
    sum+=a
    while True:
        b= float(input())
        if b ==0:
            break
        else:
            sum+=b
            ct+=1
    print(sum/ct)




