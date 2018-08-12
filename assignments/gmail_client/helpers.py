import MySQLdb
import dateutil.parser as parser

from apiclient import discovery
from oauth2client import file, client, tools
from httplib2 import Http


class GmailInbox:
    LABEL_ONE = 'INBOX'

    def __init__(self, scope, credentials, token):
        store = file.Storage(token)
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(credentials, scope)
            creds = tools.run_flow(flow, store)
        service = discovery.build('gmail', 'v1', http=creds.authorize(Http()))
        self.service = service

    def get_message_ids(self, user_id):
        """
        Fetch 100 latest message id from inbox
        """
        msgs = []

        response = self.service.users().messages().list(
                userId=user_id,
                labelIds=[self.LABEL_ONE, ],
                ).execute()

        msgs.extend(response['messages'])

        msg_ids = [m['id'] for m in msgs]
        return msg_ids

    def get_message_details(self, user_id, msg_ids):
        """
        Return message details of specied msg IDs
        """
        result = []

        for msg_id in msg_ids:
            temp_dict = {}
            temp_dict['msg_id'] = msg_id

            message = self.service.users().messages().get(userId=user_id, id=msg_id).execute()

            payload = message['payload']
            headers = payload['headers']

            for header in headers:
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

    def get_all_inbox_msg_ids(self, user_id):
        """
        Fetch all msg-IDs from inbox
        """
        msgs = []

        response = self.service.users().messages().list(
                userId=user_id,
                labelIds=[self.LABEL_ONE, ],
                ).execute()

        if 'messages' in response:
            msgs.extend(response['messages'])

        while 'nextPageToken' in response:
            page_token = response['nextPageToken']

            response = self.service.users().messages().list(
                    userId=user_id,
                    labelIds=[self.LABEL_ONE, ],
                    pageToken=page_token
                    ).execute()

            msgs.extend(response['messages'])

        msg_ids = [m['id'] for m in msgs]

        return msg_ids

    def mark_as_read(self, user_id, msg_ids):
        for msg_id in msg_ids:
            self.service.users().messages().modify(
                userId=user_id,
                id=msg_id,
                body={'removeLabelIds': ['UNREAD']}).execute()

        return None

    def mark_as_unread(self, user_id, msg_ids):
        for msg_id in msg_ids:
            self.service.users().messages().modify(
                userId=user_id,
                id=msg_id,
                body={'addLabelIds': ['UNREAD']}).execute()

        return None

    def archive_message(self, user_id, msg_ids):
        for msg_id in msg_ids:
            self.service.users().messages().modify(
                userId=user_id,
                id=msg_id,
                body={'removeLabelIds': ['INBOX']}).execute()

        return None

    def unarchive_message(self, user_id, msg_ids):
        for msg_id in msg_ids:
            self.service.users().messages().modify(
                userId=user_id,
                id=msg_id,
                body={'addLabelIds': ['INBOX']}).execute()

        return None

    def add_label(self, user_id, msg_ids, label):
        for msg_id in msg_ids:
            self.service.users().messages().modify(
                userId=user_id,
                id=msg_id,
                body={'addLabelIds': [label]}).execute()

        return None


class Database:
    def __init__(self, db_host, db_user, db_password, db_name):
        self.connection = MySQLdb.connect(db_host, db_user, db_password, db_name)
        self.cursor = self.connection.cursor()

    def create_table(self, query):
        self.cursor.execute(query)

    def is_table_exist(self, table):
        """
        check if specified table exist in database
        """
        self.cursor.execute("SHOW TABLES LIKE '{}'".format(table))
        result = self.cursor.fetchone()
        return True if result else False

    def insert_value(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()

    def insert_values(self, query, data):
        """
        Take data as dict & save all info in table as per query
        """
        try:
            self.cursor.executemany(query, data)
            self.connection.commit()
        except:
            self.connection.rollback()

    def fetch(self, query):
        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(query)

        return cursor.fetchall()

    def __del__(self):
        self.connection.close()
