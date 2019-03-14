import smtplib
from email.mime.text import MIMEText
from email.header import Header

f = open("/etc/shadowsocks.json", 'r+')
for line in f:
    print line
    content = line
f.close()

sender = 'from@banwagong.com'
receivers = ["eagle_air@126.com"]

message = MIMEText(content, 'plain', 'utf-8')
#message = MIMEText('This is a import message, very important!', 'plain', 'utf-8')
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