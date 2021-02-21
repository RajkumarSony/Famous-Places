"""
## ===> SMS in Python <==##

==> Your New Mobile No. : +14793482870
==> Account SID : AC7efdb19a99ca338848352f32d5a21002
==> Account Token : 9f323a389660d99ec75f6077bd6a725d
"""

!pip install twilio

import os
import random
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure

OTP = random.randint(1000,9999)
print(OTP)

account_sid = 'AC7efdb19a99ca338848352f32d5a21002'
auth_token = '9f323a389660d99ec75f6077bd6a725d'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Your OTP is "+str(OTP),
                     from_='+14793482870',
                     to='+918252444848'
                 )

print(message.sid)