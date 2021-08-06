import requests
import re
url = "https://www.youtube.com/channel/UCyUZg_cPAg1-QjPHKJu20ZA"
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    pattern = input("想找啥：")
    if pattern in htmlfile.text:
        print(f'搜尋{pattern}大成功\(0w0)/')
    else:
        print(f'搜尋{pattern}大失敗')
    name = re.findall(pattern,htmlfile.text)
    if name!=None:
        print(f'{pattern}出現 {len(name)} 次')
    else:
        print(f'{pattern}出現 0 次')
else:
    print("網頁擷取失敗!!!")