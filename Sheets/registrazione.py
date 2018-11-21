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

name = input("Nome: ")
surname = input("Cognome: ")
birth_date = input("Data di nascita: ")
row = [name, surname, birth_date]
sheet.insert_row(row, 1)