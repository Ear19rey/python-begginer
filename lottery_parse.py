import requests
from bs4 import BeautifulSoup as bs
url = 'http://www.taiwanlottery.com.tw/'
html = requests.get(url)
sp = bs(html.text,'html.parser')

data1 = sp.select('#rightdown')
data2 = data1[0].find('div',{'class':'contents_box02'})
data3 = data2.find_all('div',{'class':'ball_tx'})
data4 = data2.find('div',{'class':'ball_red'})
print(data4)

ball=[]
for i in data3:
    ball.append(i.text)
print(ball)

print('開出順序：',end='')
for i in range(6):
    print(ball[i],end=' ')

print('\n大小順序：',end='')
for i in range(6,len(ball)):
    print(ball[i],end=' ')

print(f'\n第二區：{data4.text}')