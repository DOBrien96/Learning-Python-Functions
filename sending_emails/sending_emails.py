from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from pathlib import Path
import smtplib

template = Template(Path("templates.html").read_text())

message = MIMEMultipart()
message["from"] = "Dylan O'Brien"
message["to"] = "testemail@gmail.com"
message["subject"] = "This is a test"
body = template.substitute({ "name": "John" })
message.attach(MIMEText(body, "html"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo() #Starts communication with the website
    smtp.starttls() #Encrypts your email
    smtp.login("myemailusername@gmail.com", "myemailpassword")
    smtp.send_message(message)
    print("Email successfully sent :)")