import smtplib
from email.mime.text import MIMEText
from email.header import Header

maxPort = 60000
f = open("/etc/shadowsocks.json", 'r')
i = 1
content = ""
for line in f:
    if i == 3:
        num = line.split(":")
        num1 = num[1].split(",")
        portNumber = int(num1[0])+1
        if portNumber > maxPort:
            portNumber = 5050
        content = '"server_port":'+str(portNumber)+','
    i = i+1
f.close()

print content

with open('/etc/shadowsocks.json', 'r') as f:
    lines = f.readlines()
with open('/etc/shadowsocks.json', 'w') as fw:
    for line in lines:
        if "server_port" in lines:
            line = content
            print "line is "+line
        fw.write(line)




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