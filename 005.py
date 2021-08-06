s = float(input("enter the size(liter):"))
n = int(input("enter the number:"))
if s<=1:
    print('$','%.2f'%(0.10*n))
else:
    print('$','%.2f'%(0.25*n))