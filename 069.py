n = int(input())
sum = 3
print(1,sum)
for i in range(1,n):
    add = 4/(2*i*(2*i+1)*(2*i+2))*((-1)**(i-1))
    sum+=add
    print(i+1,sum)