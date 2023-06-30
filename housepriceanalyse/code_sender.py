import smtplib
from email.mime.text import MIMEText
from email.header import Header
import random
# 发送邮箱验证码

class IdentifyCode(object):
    def __new__(cls, receiver=None):
        if receiver is None:
            raise Exception('Please input receiver email address.\n')
        # 随机数串生成
        num_ls = [chr(random.randint(0, 9) + 48) for i in range(6)]
        # print(num_ls)

        # 发件人邮箱
        sender = '2417856490@qq.com'
        # STMP授权码
        password = 'efvaglrlofqaecde'
        # 邮件内容
        subject = '请查收您的验证码'
        message = '您的验证码是：' + "".join(num_ls)
        # print(message)

        # 创建一个MIMEText对象，处理邮件正文
        msg = MIMEText(message, 'plain', 'utf-8')
        msg['From'] = Header(sender)
        msg['To'] = Header(receiver)
        msg['Subject'] = Header(subject)

        # noinspection PyBroadException
        try:
            # 连接SMTP服务器
            server = smtplib.SMTP('smtp.qq.com', 25)
            # 登录发件人邮箱
            server.login(sender, password)
            # 发送邮件
            server.sendmail(sender, receiver, msg.as_string())
            # print('邮件发送成功')
            server.quit()
            return "".join(num_ls)
        except Exception as e:
            raise Exception('Failed to send email.\n')
            # print('邮件发送失败:', str(e))
