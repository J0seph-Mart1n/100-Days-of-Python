from twilio.rest import Client
import os
import smtplib

account_sid = os.environ["account_sid"]
auth_token = os.environ["auth_token"]
my_email = "jmkl0987@gmail.com"
password = os.environ["EMAIL_PASSWORD"]

class NotificationManager:
    #Manages the notification of low price alert
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    #Sends SMS to user
    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_='+16562184044',
            to='+yournumber',
        )
        # Prints if successfully sent.
        print(message.sid)

    #Sends gmail to user
    def send_email(self, message, to_email):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f"Subject: Low price alert!!\n\n{message}"
            )