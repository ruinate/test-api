import smtplib
from email.mime.text import MIMEText


class SendEmail:

    def send_main(self, a, b):
        msg_from = 'asdfghjklz023@qq.com'  # 发送方邮箱
        passwd = 'ntonfuaffmgcbbih'  # 填入发送方邮箱的授权码(填入自己的授权码，相当于邮箱密码)
        msg_to = ['a7658200996@163.com']  # 收件人邮箱

        subject = "接口测试"  # 主题
        content = "通过用例数:" + a + "个"  "失败用例数:" + b + "个"

        # 生成一个MIMEText对象（还有一些其它参数）
        # _text_:邮件内容
        msg = MIMEText(content)
        # 放入邮件主题
        msg['Subject'] = subject
        # 也可以这样传参
        # msg['Subject'] = Header(subject, 'utf-8')
        # 放入发件人
        msg['From'] = msg_from
        # 放入收件人
        msg['To'] = 'a7658200996@163.com'
        # msg['To'] = '发给你的邮件啊'
        try:
            # 通过ssl方式发送，服务器地址，端口
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            # 登录到邮箱
            s.login(msg_from, passwd)
            # 发送邮件：发送方，收件方，要发送的消息
            s.sendmail(msg_from, msg_to, msg.as_string())
            print('成功')
        except s.SMTPException as e:
            print(e)
        finally:
            s.quit()
