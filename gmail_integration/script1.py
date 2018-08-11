import os

from gmail_client import GmailInbox
from database import Database

SCOPE = 'https://www.googleapis.com/auth/gmail.modify'
USER_ID = 'me'

DB_HOST = '127.0.0.1'
DB_USER = os.environ.get('DATABASE_USER')
DB_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DB_NAME = 'gmail_inbox'
TABLE_NAME = 'Inbox'


def inbox_msg_details():
    """
    Fetch lates 100 message-id from gamil inbox.
    Returm message details of each ID.
    """
    inbox = GmailInbox(SCOPE)

    # msg_ids = inbox.get_all_inbox_msg_ids(USER_ID)

    # Lets fetch only 100 message IDs
    msg_ids = inbox.get_message_ids(USER_ID)

    msg_details = inbox.get_message_details(USER_ID, msg_ids)

    return msg_details


def create_table(db, table):
    query = """
        CREATE TABLE {}
        (`id` INT AUTO_INCREMENT PRIMARY KEY,
        `msg_id` VARCHAR(255),
        `from` VARCHAR(255),
        `to` VARCHAR(255),
        `subject` TEXT,
        `snippet` TEXT,
        `date` date)
        """.format(table)

    print "Creating {} table in {} DB\n".format(TABLE_NAME, DB_NAME)
    db.create_table(query)

    return None


def insert_data(db, table):
    "Fetch data from gmail & insert in DB"

    query = """
        INSERT INTO {}
        (`msg_id`, `from`, `to`, `subject`, `snippet`, `date`)
        VALUES
        (%(msg_id)s, %(from)s, %(to)s, %(subject)s, %(snippet)s, %(date)s)
        """.format(table)

    print "Fetching data from Gmail\n"
    data = inbox_msg_details()

    print "Inserting data in database\n"
    db.insert_values(query, data)

    return None


def main():

    db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    if not db.is_table_exist(TABLE_NAME):
        create_table(db, TABLE_NAME)

    insert_data(db, TABLE_NAME)
    print "Done\n"


if __name__ == "__main__":
    main()
