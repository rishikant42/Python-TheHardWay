import requests
import os

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox7849da27e85e4394be8eb250b2e51571.mailgun.org/messages",
        auth=("api", os.environ['mapi']),
        data={"from": "rishikant <mailgun@sandbox7849da27e85e4394be8eb250b2e51571.mailgun.org>",
              "to": ["rishi.kant@doublespring.com", "rshkntshrm@gmail.com"],
              "subject": "Python Test",
              "text": "Testing some Mailgun awesomeness!"})

send_simple_message()
