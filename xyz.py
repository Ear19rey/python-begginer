a = float(input())
b = float(input())
c = float(input())
t = b**2-4*a*c
if t>=0:
    print("x1=",(-b+(b**2-4*a*c)**(1/2))/2*a)
    print("x2=",(-b-(b**2-4*a*c)**(1/2))/2*a)
else:
    print("none")