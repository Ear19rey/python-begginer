from random import sample

a=input("Please enter a filename:")
with open (a,"r") as f:
    word=f.read().replace('\n',' ').split(' ')
    print(word)

rc=sample(word,2)
while True:
    if len(rc[0])>=3 and len(rc[1])>=3 and 10>=len(rc[0]+rc[1])>=8:
        password = rc[0].capitalize()+rc[1].capitalize()
        print("The random password is :",password)
        break
    else:
        rc=sample(word,2)
