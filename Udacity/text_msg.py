from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9fec95484d85a67cbbb67c87fbc743f3"
# Your Auth Token from twilio.com/console
auth_token  = "1d88c36509908108b54f68e23229fb9b"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918126673095", 
    from_="+12566678909",
    body="Hello! this is Ritesh. This is a programmable sms send using Python!")

print(message.sid)