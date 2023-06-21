from twilio.rest import Client
from config import account_sid, auth_token

client = Client(account_sid, auth_token)

call = client.messages.create(
    to="", #The phone number of the person you want to send a message to.
    from_="+13132546997", #Our twilio number goes here.
    body="This is our first message" #The message.
)
