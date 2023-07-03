"""
Python的File(文件)方法
"""

file = '../py_file/game.txt'
# f = open(file,'x')
f = open(file,'w',encoding='utf-8')
fnum=f.write("测试一下\n下一行\n下一行")
f2 = open(file,'r+',encoding='utf-8')
f2.write("放到开头")
print(fnum)#输出12
print(f2.read(-1))

f.close(),f2.close()

"""
file: 必需，文件路径（相对或者绝对路径）。
mode: 可选，文件打开模式 常用；w w+ a a+ wb wb+ ab ab+ 
buffering: 设置缓冲
encoding: 一般使用utf8
errors: 报错级别
newline: 区分换行符
closefd: 传入的file参数类型
opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。
"""

