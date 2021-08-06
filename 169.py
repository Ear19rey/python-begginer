def StrEditDist(s,t):
    if len(s)==0:
        return len(t)
    elif len(t)==0:
        return len(s)
    else:
        cost=0
        if s[-1] != t[-1]:
            cost=1
        d1=StrEditDist(s[:-1],t)+1
        d2=StrEditDist(s,t[:-1])+1
        d3=StrEditDist(s[:-1],t[:-1])+cost
        return min(d1,d2,d3)

def main():
    s = input("Enter a string ('v') :")
    t = input("Enter another string (oEo) :")
    print(f'Edit distance between {s} and {t} is {StrEditDist(s,t)}')

if __name__=="__main__":
    main()