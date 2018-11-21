import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import unicodedata

def out(value):
    pp.pprint(value)
    print("-"*100)

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("api.json", scope)
client = gspread.authorize(creds)

sheet = client.open("test").sheet1
all_rec = sheet.get_all_records()

pp = pprint.PrettyPrinter()
out(all_rec)

row = sheet.row_values(3)
out(row)

col = sheet.col_values(2)
out(col)

cell = sheet.cell(6,4).value
out(cell)

sheet.update_cell(6,2,"Grandi")

row = ["Giulio", "Pacifici", "29/02/1992", 0]
index = 8
sheet.insert_row(row, index)
#sheet.delete_row(row, index)
print(sheet.row_count)