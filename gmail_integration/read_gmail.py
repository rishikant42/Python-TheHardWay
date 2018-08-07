import base64
import time
import dateutil.parser as parser

from apiclient import discovery, errors
from oauth2client import file, client, tools
from httplib2 import Http

SCOPES = 'https://www.googleapis.com/auth/gmail.modify'
USER_ID =  'me'
LABEL_ONE = 'INBOX'
#label_id_two = 'UNREAD'

def get_or_create_creds():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    return creds

def get_inbox_msg_ids():
    msgs = []

    creds = get_or_create_creds()
    service = discovery.build('gmail', 'v1', http=creds.authorize(Http()))
    response = service.users().messages().list(
            userId=USER_ID,
            labelIds=[LABEL_ONE, ],
            ).execute()

    msgs.extend(response['messages'])

    msg_ids = [m['id'] for m in msgs]
    return msg_ids[:5]

def get_message_details():
    msg_ids = get_inbox_msg_ids()
    creds = get_or_create_creds()
    service = discovery.build('gmail', 'v1', http=creds.authorize(Http()))

    for msg_id in msg_ids:
        temp_dict = { }
        message = service.users().messages().get(userId=USER_ID, id=msg_id).execute()

        payload = message['payload']
        headers = payload['headers']

        for header in headers: # getting the Subject
            if header['name'] == 'Subject':
                msg_subject = header['value']
                temp_dict['Subject'] = msg_subject.encode('utf-8')

            elif header['name'] == 'Date':
                msg_date = header['value']
                date_parse = (parser.parse(msg_date))
                m_date = (date_parse.date())
                temp_dict['Date'] = str(m_date).encode('utf-8')

            elif header['name'] == 'From':
                msg_from = header['value']
                temp_dict['Sender'] = msg_from.encode('utf-8')

            elif header['name'] == 'To':
                msg_from = header['value']
                temp_dict['Receiver'] = msg_from.encode('utf-8')

            else:
                pass
        print temp_dict

get_message_details()
