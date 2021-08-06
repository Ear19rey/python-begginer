n=input()
a = 0
b = len(n)
for i in range(b):
    a += int(n[i])*(2**(b-1-i))
    print(a)