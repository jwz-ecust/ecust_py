# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText

mail_host = 'smtp.qq.com'
mail_user = "897978644@qq.com"
mail_pass = "ojczemvmsmdbbaij"

me = "jwz-ecust" + '<' + mail_user + '>'
to = "aaronzjw6@gmail.com"

msg = MIMEText("test", _subtype='plain', _charset='utf-8')
msg['Subject'] = 'Hello World'
msg["From"] = me
msg['To'] = to
try:
    server = smtplib.SMTP()
    server.connect(mail_host)
    server.login(mail_user, mail_pass)
    server.sendmail(me, to, msg.as_string())
    server.close()
    print "邮件发送成功"
except Exception as e:
    print e
