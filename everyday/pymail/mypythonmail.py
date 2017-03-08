# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = "13162582627@163.com"
pwd="zjw865614"
receivers = ['897978644@qq.com', "aaronzjww@icloud.com", "1258327833@qq.com"]

msg = MIMEText("张佳伟", _subtype='plain', _charset='utf-8')
msg["Subject"] = Header("A mail send by python")
msg["From"] = "from python"
msg["To"] = receivers

s = smtplib.SMTP("smtp.163.com", port=25, timeout=30)
s.login("13162582627@163.com", "zjw865614")
s.sendmail(sender, receivers, msg.as_string())
s.close()
