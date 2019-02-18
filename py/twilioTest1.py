# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:13:33 2019

@author: Administrator
"""

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC5f4b0f2263e11222efdbcc4893f39719'
auth_token = 'fd990e848563b300dafe028817bded6e'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+16788206397',
                     to='+8618324519124'
                 )

print(message.sid)
