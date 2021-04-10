# coding=utf-8
# 配置邮件
from email.mime.text import MIMEText  # 只能发送正文
from email.mime.multipart import  MIMEMultipart  # 可以发送附件和正文
import smtplib # 邮件系统
from common import readConfig


class SendEmail():
    def __init__(self):
        self.host = readConfig.Readconfig.qq_ini('email_host')
        self.sender = readConfig.Readconfig.qq_ini('email_sender')
        self.recevier = readConfig.Readconfig.qq_ini('email_receiver')
        self.pwd = readConfig.Readconfig.qq_ini('email_pwd')

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


