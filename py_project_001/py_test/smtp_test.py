"""Python网络编程 SMTP协议"""
"""SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议,
它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式。
"""

import smtplib #导入包
from email.mime.text import MIMEText
from email.header import Header
from email_test import base_message




smtp_addr = 'smtp.qq.com'
send_addr = '2763503952@qq.com'
send_password = 'qkdclgdtkksadfdg'
rev_addr = 'shuangzibingchuan@gmail.com'

smtpObj = smtplib.SMTP_SSL(smtp_addr,465)#创建smtp类
"""
这里使用SMTP协议发送邮件，括号里面为对应的地址，下面列举常用的邮箱地址：
QQ:smtp.qq.com 端口：465
Gmail:smtp.gmail.com (SSl启用)端口：465
"""


smtpObj.login(user=send_addr,password=send_password)
"""
- user:发送者的账号
- password：发送者的SMTP密钥
"""

text = 'Python测试'
mode = 'plain'
text1 = """
    <p>Python 邮件发送测试...</p>
    <p><a href="http://www.runoob.com">这是一个链接</a></p>
    """
mode1 = 'html'
smtpObj.sendmail(from_addr=send_addr,to_addrs=[rev_addr]
                     ,msg=base_message(text1,mode1).as_string())
"""
- from_addr : 发送地址
- to_addrs  : 接受地址列表
- msg       : 发送内容文本
"""
smtpObj.quit()#退出smtp








