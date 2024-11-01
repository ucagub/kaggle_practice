import gspread
# from google.oauth2.service_account import Credentials

# Define the scope
# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Authenticate using the service account key file
# creds = Credentials.from_service_account_file('../gsheets.json', scopes=scope)
# client = gspread.authorize(creds)

gc = gspread.service_account()

# Open a spreadsheet by URL
spreadsheet = gc.open("test_api") 
# spreadsheet = gc.open("Copy of 01_LAM Guide with Leveling Tool_LAM_21Oct2024") 
# spreadsheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/1opCXDJu2ssY8mD3hQTE4GAoMCHiPvalK/edit?gid=871405699") 

# Get all worksheets in the spreadsheet
worksheets = spreadsheet.worksheets()

# Print the names of all worksheets
for worksheet in worksheets:
    print(worksheet.title)

# Select a worksheet (uncomment if needed)
# worksheet = spreadsheet.sheet1  # or use .get_worksheet(index)

# Read values from a range (uncomment if needed)
# values = worksheet.get('A1:B10')
# print(values)