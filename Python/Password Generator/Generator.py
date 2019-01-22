import gspread
import string
import random
from oauth2client.service_account import ServiceAccountCredentials

#Used to communicate with Google Sheets
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Password List").sheet1

rows = len(sheet.col_values(1))

def generator(website):
    password = ""

    # Sets all requirements
    numbers = int(input("How many numbers are required?\n"))
    symbols = int(input("How many symbols (!, #, %, etc.) are required?\n"))
    length = int(input("How long does the password need to be?\n"))
    print("Processing.....")

    # Random string of lowercase letters
    seed = ''.join(random.choice(string.ascii_lowercase) for i in range(length))

    # Assumes website does not take numbers or symbols
    if(numbers == 0 and symbols == 0 and symbols == 0):
        password = seed.join(random.choice(string.ascii_lowercase) for i in range(length))
        print(password)

    


generator(input("Please enter a website:\n"))
