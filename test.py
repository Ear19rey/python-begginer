content='''kokokok
lololo
'''
with open('kokoko.txt','r+',encoding='utf-8') as f:
    f.write(content)
    f.seek(0)
    a = f.read()
    print(a)