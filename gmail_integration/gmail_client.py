import base64
import time
import dateutil.parser as parser

from apiclient import discovery, errors
from oauth2client import file, client, tools
from httplib2 import Http


class GmailInbox:
    LABEL_ONE = 'INBOX'

    def __init__(self, scope):
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', scope)
            creds = tools.run_flow(flow, store)
        service = discovery.build('gmail', 'v1', http=creds.authorize(Http()))
        self.service = service

    def get_message_ids(self, user_id):
        msgs = []

        response = self.service.users().messages().list(
                userId=user_id,
                labelIds=[self.LABEL_ONE, ],
                ).execute()

        msgs.extend(response['messages'])

        msg_ids = [m['id'] for m in msgs]
        return msg_ids[:2]

    def get_message_details(self, user_id, msg_ids):
        result = []

        for msg_id in msg_ids:
            temp_dict = { }
            temp_dict['msg_id'] = msg_id

            message = self.service.users().messages().get(userId=user_id, id=msg_id).execute()

            payload = message['payload']
            headers = payload['headers']

            for header in headers: # getting the Subject
                if header['name'] == 'Subject':
                    msg_subject = header['value']
                    temp_dict['subject'] = msg_subject.encode('utf-8')

                elif header['name'] == 'Date':
                    msg_date = header['value']
                    date_parse = (parser.parse(msg_date))
                    m_date = (date_parse.date())
                    temp_dict['date'] = str(m_date).encode('utf-8')

                elif header['name'] == 'From':
                    msg_from = header['value']
                    temp_dict['from'] = msg_from.encode('utf-8')

                elif header['name'] == 'To':
                    msg_from = header['value']
                    temp_dict['to'] = msg_from.encode('utf-8')

                else:
                    pass

                temp_dict['snippet'] = message['snippet'].encode('utf-8')

            result.append(temp_dict)
        return result

    def mark_as_read(self, user_id, msg_ids):
        for msg_id in msg_ids:
            self.service.users().messages().modify(
                userId=user_id,
                id=msg_id,
                body={ 'removeLabelIds': ['UNREAD']}).execute()

        return None

    def mark_as_unread(self, user_id, msg_ids):
        for msg_id in msg_ids:
            self.service.users().messages().modify(
                userId=user_id,
                id=msg_id,
                body={ 'addLabelIds': ['UNREAD']}).execute()

        return None

    def archive_message(self, user_id, msg_ids):
        for msg_id in msg_ids:
            self.service.users().messages().modify(
                userId=user_id,
                id=msg_id,
                body={ 'removeLabelIds': ['INBOX']}).execute()

        return None

    def unarchive_message(self, user_id, msg_ids):
        for msg_id in msg_ids:
            self.service.users().messages().modify(
                userId=user_id,
                id=msg_id,
                body={ 'addLabelIds': ['INBOX']}).execute()

        return None

    def add_label(self, user_id, msg_ids, label):
        for msg_id in msg_ids:
            self.service.users().messages().modify(
                userId=user_id,
                id=msg_id,
                body={ 'addLabelIds': [label]}).execute()

        return None
