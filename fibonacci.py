def rec_fibo(n):
    if n==0 or n==1:
        return n
    else:
        return rec_fibo(n-1)+rec_fibo(n-2)

def ite_fibo(m):
    total=[0,1]
    if m <=1:
        return total[m]
    for i in range(1,m):
        total.append(total[-1]+total[-2])
    return total[-1]


