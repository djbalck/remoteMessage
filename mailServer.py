import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'from@banwagong.com'
receivers = ["zhangdejun@apusapps.com"]

message = MIMEText('This is a import message, very important!', 'plain', 'utf-8')
message['From'] = Header("dj",'utf-8')
message['To'] = Header('dj','utf-8')

subject = "Python mail test"
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "send mail succes!"
except smtplib.SMTPException:
    print "error :  Can't send email"