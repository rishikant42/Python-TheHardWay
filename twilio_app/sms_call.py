from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

# Find these values at https://twilio.com/user/account
client = Client(account_sid, auth_token)

my_msg = "Hello world"

message = client.messages.create(to=my_cell, from_=my_twilio,
                                     body=my_msg)

call = client.calls.create(to=my_cell,
                            from_=my_cell,
                            url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
print(call.sid)
