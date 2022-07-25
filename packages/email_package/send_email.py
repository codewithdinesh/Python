
from multiprocessing import AuthenticationError
import smtplib

# Specify SMTP Port
port = 2525

# Host Name of SMTP server
host = "smtp.mailtrap.io"

# email auth
email ="8f2c30e93febba"


# Specify the sender email
sender = "from@example.com"

# sender password
password = "10755d9d291d85"

# specify receiver email
receiver = "to@example.com"

# Subject
Subject = "Send Email Testing using Python"

# message
msg = "This is a test e-mail message."

# specify message
message = f"""\
Subject: 
To: {receiver}
From: {sender}
Subject:{Subject}
{msg}
"""

with smtplib.SMTP(host, port) as server:
    server.login(email, password)
    server.sendmail(sender, receiver, message)
    print("Message sent successfully..")
