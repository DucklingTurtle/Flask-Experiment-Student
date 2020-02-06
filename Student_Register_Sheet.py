import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('google-database.json', scope)
client = gspread.authorize(creds)
# s_r = client.open("Student_Register_Database").sheet1
# worksheet = sheet.get_worksheet(0)