"""Python的OS文件/目录方法"""
"""
常用的OS方法：
os.listdir(path)：返回指定path下的文件名称或者文件夹名称
os.mkdir(path[,mode]): 以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。
os.open(file, flags[, mode])：打开一个文件，并且设置需要的打开选项，mode参数是可选的
os.remove(path)：删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。
os.rename(src, dst)：重命名文件或目录，从 src 修改为 dst
os.replace(src,dst):重命名文件或者目录
os.path:os的path模块
"""

import os
file = '../py_file/game.txt'
filename = os.path.basename(file)
print(filename) #输出game.txt
print(os.path.splitext(filename))#输出('game', '.txt')
