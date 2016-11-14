def send_html_mail_file(self, params, is_debug=0):
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    import smtplib
    import random
    from email.mime.text import MIMEText

    if is_debug:
        mail_host = const.SYSTEM_EMAIL_TEST['SMTP_HOST']  # 设置服务器
        mail_user = const.SYSTEM_EMAIL_TEST['SMTP_USER']  # 用户名
        mail_pass = const.SYSTEM_EMAIL_TEST['SMTP_PASS']  # 口令
        mail_from = const.SYSTEM_EMAIL_TEST['FROM_EMAIL']
        mail_name = const.SYSTEM_EMAIL_TEST['FROM_NAME']

    else:
        mail_host = const.SYSTEM_EMAIL['SMTP_HOST']  # 设置服务器
        mail_user = const.SYSTEM_EMAIL['SMTP_USER']  # 用户名
        mail_pass = const.SYSTEM_EMAIL['SMTP_PASS']  # 口令
        mail_from = const.SYSTEM_EMAIL['FROM_EMAIL']
        mail_name = const.SYSTEM_EMAIL['FROM_NAME']

        num = random.randint(0, 10)
        system_users = const.SYSTEM_EMAIL_USER
        mail_user = system_users[num]
        mail_from = mail_user

    to = params['to']
    cc = ''
    bcc = ""

    files = ''
    if 'files' in params:
        files = params['files']

    try:
        msg = MIMEMultipart()

        content = MIMEText(
            params['msg'], _subtype='html', _charset='utf-8')  # plain
        msg.attach(content)

        if type(files) == list and len(files):
            for file in files:
                path = str(file['path'])
                if os.name is not 'posix':  # 非 linux系统
                    ipos = path.find("/")
                    if ipos > -1:
                        path = path.replace("/", "\\")
                        print [path]
                att1 = MIMEText(open(path, 'rb').read(), 'base64', 'gb2312')
                att1["Content-Type"] = 'application/octet-stream'
                att1["Content-Disposition"] = 'attachment; filename="' + \
                    str(file['filename']) + \
                    '"'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
                msg.attach(att1)

        me = mail_name + "<" + mail_from + ">"
        msg['Subject'] = params['title']
        msg['From'] = me
        msg['To'] = to
        msg['Cc'] = cc
        msg['Bcc'] = bcc
        to_list = str(to).split(";")

        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, [to_list, cc, bcc], msg.as_string())
        server.close()
        return {"error": False, "error_info": '', "mail_user": mail_user}
    except Exception, e:
        print str(e)
        return {"error": True, "error_info": str(e), "mail_user": mail_user}
