from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token" #your token generated on your twilio account

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="your registered number", 
    from_="your's twilio number",
    body="Hello! this is Ritesh. This is a programmable sms send using Python!")

print(message.sid)
