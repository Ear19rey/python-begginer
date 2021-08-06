import csv
with open(r'D:\Download\109期末考\20210610.csv',newline='') as f:
    f=csv.reader(f)
    a=[] #給符合條件的資料裝
    for i in f:
        if i[1]==" 2262" and ' 11:25'>=i[2]>=' 10:55':
            i[1]=i[1].replace(' 2262',' 全聯南華店')
            a.append((i[0]+i[2]+i[1]).split(' '))
            with open(r'new.csv','w',newline='') as nw:
                writer = csv.writer(nw)
                writer.writerow(['行動電話號碼','入場時間','場所名稱'])
                for j in a:
                    writer.writerow(j)