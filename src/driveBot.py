# importing libraries and modules
import gspread
import os
import pandas as pd
from dotenv import load_dotenv

# loading environment variables
load_dotenv()

class DriveBot: # class to create a Drive bot
    def __init__(self): # constructor
        self.gc = gspread.service_account(filename='\\Users\\macha\\Documents\\dev\\smart_cashbot\\google_credentials.json') # creating a bot object

    def get_data(self):
        sheet_key = os.getenv('SHEET_KEY')
        sh = self.gc.open_by_key(sheet_key)
        worksheet = sh.sheet1
        dataframe = pd.DataFrame(worksheet.get_all_records())
        return dataframe
