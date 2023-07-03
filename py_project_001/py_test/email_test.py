from email.mime.text import MIMEText
from email.header import Header


def base_message(text:str,mode:str):
    message=MIMEText(_text=text, _subtype=mode, _charset='utf-8')
    """
    _text is 邮件内容，可以是html.
    _subtype is 文字模式一般是plain.
    _charset is 编码格式
    """
    message['From']=Header(s="ABC<2763503952@qq.com>")  # 发送者
    message['To']=Header(s="测试", charset='utf-8')  # 接收者
    """
     Optional s is the initial header value
     Optional charset serves two purposes
    """
    subject='Python SMTP 邮件测试'
    message['Subject']=Header(subject, 'utf-8')  # 邮箱标题
    """
    Return the entire formatted message as a string
    """
    return message