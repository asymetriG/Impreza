import json
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_forget_password_mail(subject,message,to_email):
    email = "imprezayazlab@outlook.com"
    password = "araba1478"
    
    
    msg = MIMEMultipart()
    
    msg["From"] = email
    msg["To"] = to_email
    msg["Subject"] = subject
    
    body = message
    
    msg.attach(MIMEText(body,"plain"))
    
    
    server = smtplib.SMTP("smtp-mail.outlook.com",587)
    
    server.starttls()
    
    server.login(email,password)
    
    text = msg.as_string()
    
    server.sendmail(email,to_email,text)
    
    server.quit()
    
    
if __name__=="__main__":
    
    send_forget_password_mail("Deneme maili konusu","Ya mert","omerkomni@gmail.com")
