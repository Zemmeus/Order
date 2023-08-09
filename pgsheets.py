import pygsheets
import gspread
path='studious-rhythm-390907-798ae3194f44.json'
gc = pygsheets.authorize(service_account_file=path)
print(gc.spreadsheet_titles())
sh = gc.open('pythontest') # Open the google sheet phthontest
wks = sh[0] # select the first sheet 
wks.update_col(2,['ab','casd','1f']) # add list to 2nd column
data1 = ["Рамиль123"]

data = {'name': 'asd', 'age': '12', 'f': '1', 'Forma': '2', 'Position': '3', 'OPGinhale': '93', 'OPGouthale': '89', 'OG': '101', 'Formula': '85C', 'ID': 1915805542, 'UserName': 'Рамиль'}
x = [[i for i in data.values()]]
wks.append_table(x, start='A2', end=None, 
    dimension='ROWS', overwrite=True)



# service_account = gspread.service_account(path) # Укажите путь к файлу JSON сервисного аккаунта
# gs = service_account.open("pythontest") # Тут название гугл таблицы
# list_name = "0" # Тут название листа

# data = [1]

# x = [[i for i in data.values()]]
# gs.values_append(data, {'valueInputOption': 'USER_ENTERED'}, {'values': x})
