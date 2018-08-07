from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file as oauth_file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'


def main():
    """Shows basic usage of the Gmail API.

    Lists the user's Gmail labels.
    """
    store = oauth_file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    # Call the Gmail API
    results = service.users().messages().list(userId='me').execute()
    messages = results.get('messages', [])
    import ipdb; ipdb.set_trace() # BREAKPOINT
    if not messages:
        print('No messages found.')
    else:
        print('messages:')
        for message in messages:
            print("\n\n")
            print(message)
            print("\n\n")


if __name__ == '__main__':
    main()
