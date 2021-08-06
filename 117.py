#sigma xy
def sig_xy(ls1,ls2):
    total=0
    for i in range(len(ls2)):
        total+=float(ls1[i])*float(ls2[i])
    return total

#sigma x
def sig_x(ls1):
    total=0
    for i in ls1:
        total+=float(i)
    return total

#sigma x**2
def sig_xsqr(ls1):
    total=0
    for i in ls1:
        total+=float(i)**2
    return total
x_ls = []
y_ls = []
while True:
    x=input("Enter x:")
    if x!='':
        y=float(input("Enter y:"))
        x_ls.append(x)
        y_ls.append(y)
    else:
        break
m= (sig_xy(x_ls,y_ls)-sig_x(x_ls)*sum(y_ls)/len(y_ls))/(sig_xsqr(x_ls)-(sig_x(x_ls)**2/len(y_ls)))
b= sum(y_ls)/len(y_ls)-m*(sig_x(x_ls)/len(y_ls))
print(f'y = {m}x + {b}')






