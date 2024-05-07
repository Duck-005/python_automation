import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from datetime import date
import random

PORT = 587
EMAIL_SERVER = "smtp-mail.outlook.com"

SenderEmail = "SenderMail@mail.com"
SenderEmailPass = "password"

msg = EmailMessage()

def send_email(subject, Name, recieverEmail, dayCount, love_message):
    msg["Subject"] = subject
    msg["From"] = formataddr(("Yours truly", f"{SenderEmail}"))  # display name instead of email address
    msg["To"] = recieverEmail

    msg.set_content(
        f'''
        Dear {Name},
        
        Today is day {dayCount} of expressing my love to you.

        {love_message}

        Yours truly, \u2764  
        '''
        # unicode for red heart emoji --> \u2764
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:  # SMTP : simple mail transfer protocol
        server.starttls()  # tls protocol for secure transmission of data
        server.login(SenderEmail, SenderEmailPass)
        server.sendmail(SenderEmail, recieverEmail, msg.as_string())
    del msg["Subject"]  # preps for the mail to be sent to the next bakra
    del msg["From"]
    del msg["To"]

if __name__ == "__main__":
    loveMessageList = open("loveMessageList.txt", mode="r", encoding='utf-8')
    msgList = loveMessageList.readlines()

    randomList = [1, 4, 7, 10]  # starting line of each message
    loveMessage = ''
    for msgLine in range(random.choice(randomList) - 1, len(msgList)):
        if msgList[msgLine] == "\n":
            break
        else:
            loveMessage += msgList[msgLine] + '\t'

    epoch = date(2024, 5, 2)  # date of commencement of email spam
    day_count = (date.today() - epoch).days  # date lapsed since then 
    day_count += 1
    bakraDict = {"Dummy01": "testDummy01@mail.com", "Dummy02": "testDummy02@mail.com"}

    for name in bakraDict:
        send_email(
            subject="दैनिक प्रेम",
            Name=name,
            recieverEmail=bakraDict[name],
            dayCount=day_count,
            love_message=loveMessage
        )
        print("email sent to", bakraDict[name])
