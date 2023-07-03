"""Python的网络编程"""
"""客户端"""

import socket
import sys


# 创建 socket 对象

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port))

# 接收小于 1024 字节的数据
#接收TCP数据，数据以字符串形式返回，
# bufsize指定要接收的最大数据量。
msg = s.recv(1024)

s.close()

print (msg.decode('utf-8'))

"""cd进入pytest 文件夹:cd py_test"""
"""python + 文件名字 运行python文件"""
