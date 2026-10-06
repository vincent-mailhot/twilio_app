import os
from twilio.rest import Client

# Set your credentials as environment variables or replace them here
account_sid = os.environ.get("TWILIO_ACCOUNT_SID", "your_account_sid")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN", "your_auth_token")
client = Client(account_sid, auth_token)

# The TwiML URL that tells Twilio what to say or do when the call is answered
# You can use Twilio's demo URL or host your own TwiML response
twiml_url = "http://twilio.com"

call = client.calls.create(
    to="+1234567890",  # Destination phone number
    from_="+0987654321",  # Your Twilio phone number
    url=twiml_url,
)

print(f"Voice message call initiated with SID: {call.Sid}")