'''
sample code
'''
import sys

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

# spread sheet id
SAMPLE_SPREADSHEET_ID = '1jrh5KkQ-Ta6Ku1VGgXlS1dW4EjQjl1d98kyc5fPq7OU'


def get_credentials():
    store = file.Storage('token.json')
    creds = store.get()

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(
            '/Users/wararaki/.google/credentials.json',
            SCOPES
        )
        creds = tools.run_flow(flow, store)
    return creds


def main():
    # get credentials
    credentials = get_credentials()

    # authorization
    service = build('sheets', 'v4', http=credentials.authorize(Http()))

    # write sheet
    sheet = service.spreadsheets()
    request = sheet.values().update(
        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range='A1:C1',
        valueInputOption='USER_ENTERED',
        body={'values': [[1, 2, 3]]}
    )
    response = request.execute()
    print('write:')
    print(response)

    # read sheet
    request = sheet.values().get(
        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range='A1:C1'
    )
    response = request.execute()
    print('read:')
    print(response)

    return 0


if __name__ == '__main__':
    sys.exit(main())
