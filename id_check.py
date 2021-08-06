def IDcheck(id):
    a={'A':10,'J':18,'S':26,
     'B':11,'K':19,'T':27,
     'C':12,'L':20,'U':28,
     'D':13,'M':21,'V':29,
     'E':14,'N':22,'W':32,
     'F':15,'O':35,'X':30,
     'G':16,'P':23,'Y':31,
     'H':17,'Q':24,'Z':33,
     'I':34,'R':25}
    rate=[1,9,8,7,6,5,4,3,2,1,1]

    if len(id)!=10:
        return "輸入錯誤：須輸入十碼"
    elif not id[0].isalpha():
        return "輸入錯誤：第一碼須為英文"
    elif not id[1:].isdigit():
        return "輸入錯誤：後九碼須為數字"
    else:
        id = id.capitalize()
        num=str(a[id[0]])+id[1:]
        total=0
        for i in range(11):
            total+=int(num[i])*rate[i]
    if total%10==0:
        return "有效身分證字號!"
    else:
        return "無效身分證字號!"

def main():
    id=input("Enter your ID:")
    print(IDcheck(id))
if __name__=="__main__":
    main()
'''
with open("ID.txt",'r') as f:
    ids=f.readlines()
    for id in ids:
        id=id.replace('\n','')
        print(f'{id} : {IDcheck(id)}')
'''