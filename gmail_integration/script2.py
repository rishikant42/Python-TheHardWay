import os
import json

from gmail_client import GmailInbox
from database import Database

SCOPE = 'https://www.googleapis.com/auth/gmail.modify'
USER_ID = 'me'

DB_HOST = '127.0.0.1'
DB_USER = os.environ.get('DATABASE_USER')
DB_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DB_NAME = 'gmail_inbox'
TABLE_NAME = 'Inbox'

sql_map = {
    'contains': 'LIKE',
    'does_not_contain': 'NOT LIKE',
    'equal': '=',
    'not_equal': '!=',
    'less_than': '<',
    'all': 'AND',
    'any': 'OR',
}

RULE_NUMBER = "rule1"


def create_sql_fetch_query(rules_set, overall_predicate):
    """
    Read all rules, convert them in sql query form.
    Combine queries as per predicate to create a single sql query.
    """
    queries = []
    for rule in rules_set:
        field_name = rule[0]
        predicate = rule[1]
        value = rule[2]

        if predicate == 'contains' or predicate == 'does_not_contain':
            query_struct = "`{}` {} '%{}%'"
        else:
            query_struct = "`{}` {} '{}'"

        sub_query = query_struct.format(
                field_name,
                sql_map.get(predicate),
                value)

        queries.append(sub_query)

    filter_query = " {} ".format(
            sql_map.get(overall_predicate)
            ).join(queries)

    sql_query = "SELECT * FROM Inbox WHERE {}".format(filter_query)

    return sql_query


def take_action(action, msg_ids, label=None):
    """
    take specified action on msg_ids
    """
    inbox = GmailInbox(SCOPE)

    if action == "mark_as_read":
        inbox.mark_as_read(USER_ID, msg_ids)

    elif action == "mark_as_unread":
        inbox.mark_as_unread(USER_ID, msg_ids)

    elif action == "archive_message":
        inbox.archive_message(USER_ID, msg_ids)

    elif action == "unarchive_message":
        inbox.unarchive_message(USER_ID, msg_ids)

    elif action == "add_label":
        inbox.add_label(USER_ID, msg_ids, label)

    else:
        pass

    return None


def main():
    json_file = open('rules.json').read()

    rules = json.loads(json_file)

    selected_rule = rules.get(RULE_NUMBER)

    sub_rules = selected_rule.get('rules')

    action = selected_rule.get('action')

    overall_predicate = selected_rule.get('overall_predicate')

    sql_fetch_query = create_sql_fetch_query(sub_rules, overall_predicate)
    db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    print "Fetching data from database\n"
    data = db.fetch(sql_fetch_query)

    msg_ids = [i.get('msg_id') for i in data]

    print "Taking {} action\n".format(action)
    take_action(action, msg_ids)

    print "Done\n"


if __name__ == "__main__":
    main()
