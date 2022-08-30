from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account
from spot import get_data

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = '/service_account.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '152J9nfjz3QvXNQjHqkQJb48XUdApUIgu5_-hJ4BIykg'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
# result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                             range="Wise!A2:AB28").execute()
#
# values = result.get('values', [])


request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="Wise!B3:AB28", valueInputOption="USER_ENTERED", body={"values": get_data()}).execute()

# print(result)
