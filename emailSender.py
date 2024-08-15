import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from databaseFunctions import getEmailList
from datetime import datetime

def getDate():
    return datetime.now().strftime("%d %B %Y")


senderEmail = "newsbites.automated@gmail.com"
password = "TMa8Lmx6EXBFwu2F"
emailList = getEmailList()

message = MIMEMultipart("alternative")
message["Subject"] = "NewsBites: "+ getDate()
message["From"] = senderEmail
message["To"] = emailList