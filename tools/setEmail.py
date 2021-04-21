# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/16 14:11
@Author  : wanfeng
"""

# 配置邮件
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from common.rwFile import ReadConfig


class SendEmail():
    def __init__(self):
        self.host = ReadConfig.get_email('host')
        self.sender = ReadConfig.get_email('sender')
        self.recevier = ReadConfig.get_email('receiver')
        self.pwd = ReadConfig.get_email('pwd')

    def send_email(self,report_file_path):
        # 邮箱配置信息
        self.SMTP_Server = self.host
        self.sender = self.sender
        self.recevier = self.recevier
        self.pwd = self.pwd

        # 构建能装附件的容器
        self.msg = MIMEMultipart()
        self.msg['from'] = self.sender
        self.msg['to'] = ";".join(self.recevier)
        self.subject = 'QQ主题-自动发送邮件'
        self.msg['subject'] = self.subject

        # 正文内容
        with open(report_file_path,mode='r') as f:
            self.mail_body = f.read()
            f.close()

        # 创建QQ邮箱
        self.body = MIMEText(self.mail_body,'html','utf-8')
        self.msg.attach(self.body)
        # 创建附件
        self.att = MIMEText(self.mail_body,'base64','utf-8')
        self.att['Content-Type'] = 'application/ocet-stream'
        self.att['Content-Dispostion'] = 'attachment;filename="report.html"'
        self.msg.attach(self.att)
        # 构建邮箱系统
        self.smtp = smtplib.SMTP()
        self.smtp.connect(self.SMTP_Server)
        self.smtp.login(self.sender,self.pwd)
        try:
            self.smtp.sendmail(self.sender,self.recevier,str(self.msg))
            self.smtp.quit()
            print ('sendemail,success!')
        except:
            print ('sendemail,fail!')


