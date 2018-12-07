import os
import time
import re
from slackclient import SlackClient

import requests

# instantiate Slack client
token = os.environ['SLACK_TOKEN']
slack_client = SlackClient(token)
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
INFO_COMMAND = "info"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"


def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    if matches:
        return [matches.group(1), message_text.split(' ', 1)[1].strip()]
    else:
        return [None, None]
    # return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            msg = event['files'][0]['preview']
            lang = event['files'][0]['filetype']
            return [msg, event["channel"], lang]
            # user_id, message = parse_direct_mention(event["text"])
            # # user_id, message = event["text"].split(' ', 1)
            # if user_id == starterbot_id:
            #     return message, event["channel"]
    return [None, None, None]

def handle_command(command, channel, lang):
    """
        Executes bot command if the command is known
    """
    # Default response is help text for the user
    default_response = "Not sure what you mean. Try *{}*.".format(INFO_COMMAND)

    # Finds and executes the given command, filling in response
    # response = None
    # This is where you start to implement more commands!
    if str(lang) == 'python': lang = 'python2'
    if str(lang) == 'javascript': lang = 'nodejs'
    d = {
        "clientId": "4d4b392b6a10b671411d2be135f03ba7",
        "clientSecret":"d09cd470b318e5e02b4ebbb0fb10455039104c57d055b4b196d465ed7505c964",
        "script": command,
        "language":lang,
        "versionIndex":"0",
    }
    u='https://api.jdoodle.com/v1/execute'
    r = requests.post(url=u, json=d)
    response = r.json().get('output')
    # if command.startswith(INFO_COMMAND):
    #     print(command)
    #     # if 'symbol' in command:
    #     #     response = helpers.get_coins_symbol(100)
    #     # else:
    #     #     cmd, coin = command.split(' ')
    #     #     response = helpers.get_coin_info(coin)
    #     cmd, script = command.split(' ', 1)
    #     script = script.replace('&lt;', '<').replace('&gt;', '>')
    #     d = {
    #         "clientId": "",
    #         "clientSecret":"",
    #         "script": script,
    #         "language":"c",
    #         "versionIndex":"2",
    #     }
    #     u='https://api.jdoodle.com/v1/execute'
    #     r = requests.post(url=u, json=d)
    #     response = r.json()

    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel, lang = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel, lang)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
