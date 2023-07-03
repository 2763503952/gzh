"""
Python的网络编程用于TCP协议
"""
"""服务器端"""
"""
Socket又称"套接字"，
应用程序通常通过"套接字"向网络发出请求或者应答网络请求，
使主机间或者一台计算机上的进程间可以通讯
"""
import sys
import socket


#创建socket对象 AF_INET:AF_INET的主要目的是允许其他可能的网络协议或地址族
# SOCk_STREAM:SOCK_STREAM提供面向连接的稳定数据传输，即TCP协议。
# SOCK_STREAM应用在C语言socket编程中，在进行网络连接前，
# 需要用socket函数向系统申请一个通信端口。
Serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#获取本地主机名
host = socket.gethostname()
print("host:",host)
port = 9999

#绑定端口号
Serversocket.bind((host,port))
#开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。
# 该值至少为1，大部分应用程序设为5就可以了。
Serversocket.listen(5)

while True:
    #被动接受TCP客户端连接,(阻塞式)等待连接的到来
    #返回新的socket和连接地址
    sock, addr=Serversocket.accept()
    print("sock:",type(sock),sock)
    print("add:",addr)

    msg='连接到客户端了！'+'\r\n'
    #发送TCP数据，将string中的数据发送到连接的套接字。返回值是要发送的字节数量，
    #该数量可能小于string的字节大小。
    sock.send(msg.encode('utf-8'))
    sock.close()










