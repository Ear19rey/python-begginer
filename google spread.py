import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']

cr = sac.from_json_keyfile_name('./model/google_auth.json', scope)

gs = gspread.authorize(cr)

sh = gs.open('Python')
# wks  =  wks2
wks = sh.sheet1
wks2 = sh.worksheet('比奇堡')
print(wks)

#wks.update_acell('C2','美味蟹堡')
wks.update_cell(2,3,'月光光閃亮亮復仇者')

values = ['海綿寶寶', '派大星', '皮老闆']
wks.insert_row(values,1)

data1 = wks.acell('C3').value
data2 = wks.cell(3,3).value
data3 = wks.row_values(1)
data4 = wks.col_values(1)
data = wks.get_all_values()
print(data1,data2,data3,data4,data,sep='\n')