import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import unicodedata
# -*- coding: ascii -*-
def out(value):
    pp.pprint(value)
    print("-"*100)

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("api.json", scope)
client = gspread.authorize(creds)

sheet = client.open("test").sheet1
pp = pprint.PrettyPrinter()
c = 1

for obj in sheet.get_all_records():
    c+=1
    if(obj["Cognome"] == "Antoni"):
        row = sheet.row_values(c)
        out(row)
        break
    
for row in sheet.get_all_records():
    if(row["Verificato"] == 0):
        print(row["Cognome"])
