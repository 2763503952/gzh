"""Python多线程"""



"""
1.函数式定义多线程
"""
import _thread
import time

def print_time(threadName,delay):
    count = 0
    while count<5:
        time.sleep(delay)
        count += 1
        print("{0}:{1}".format(threadName,time.ctime(time.time())))
import threading

class MyThread(threading.Thread):
    def __init__(self,threadID,name,delay):
        super(MyThread, self).__init__()
        self.ThreadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print("开始线程:"+self.name)
        print_time_2(self.name,self.delay,5)
        print("退出线程:"+self.name)



def print_time_2(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1
"""
线程同步
如果多个线程共同对某个数据修改，则可能出现不可预料的结果，
为了保证数据的正确性，需要对多个线程进行同步。
"""

class MyThread2(threading.Thread):
    def __init__(self,threadID,name,delay):
        super(MyThread2, self).__init__()
        self.ThreadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print("开始线程:"+self.name)
        threadLock.acquire()#获取锁
        print_time_2(self.name,self.delay,5)
        threadLock.release()#释放锁
        print("退出线程:"+self.name)
        
def run_time_1(count:int):
    time.sleep(count)
    print("退出函数run_time_1")
def run_time_2(count:int):
    time.sleep(count)
    print("退出函数run_time_2")
class RunThread(threading.Thread):
    def run(self) -> None:
        threadLock.acquire()
        run_time_1(3)
        threadLock.release()
class RunThread2(threading.Thread):
    def run(self) -> None:
        threadLock.acquire()
        run_time_2(3)
        threadLock.release()


if __name__ == '__main__':
    # try:
    #     _thread.start_new_thread(print_time, ("Thread-1",2,))
    #     """
    #     传参：1.方法命
    #          2.方法参数
    #     """
    #     _thread.start_new_thread(print_time, ("Thread-2",4,))
    #     """
    #     输出：
    #     Thread-1:Wed Jun 28 14:33:47 2023
    #     Thread-2:Wed Jun 28 14:33:49 2023
    #     Thread-1:Wed Jun 28 14:33:50 2023
    #     Thread-1:Wed Jun 28 14:33:52 2023
    #     Thread-2:Wed Jun 28 14:33:53 2023
    #     Thread-1:Wed Jun 28 14:33:54 2023
    #     Thread-1:Wed Jun 28 14:33:56 2023
    #     Thread-2:Wed Jun 28 14:33:57 2023
    #     Thread-2:Wed Jun 28 14:34:01 2023
    #     Thread-2:Wed Jun 28 14:34:06 2023
    #     """
    # except:
    #     raise Exception("创建线程失败")
    # thread1 = MyThread(1, "Thread-1", 2)
    # thread2 = MyThread(2, "Thread-2", 3)
    #
    # #
    # thread1.start()
    # thread2.start() #开启线程 就是执行线程类的run()函数
    # print(threading.enumerate()) #返回当前正在运行的线程列表，包含一个主线程
    # print(threading.active_count())#输出3，一个主线程 两个子线程
    # thread1.join() #等待线程结束往下走
    # print(thread1.is_alive())#输出Flase，返回一个bool判断线程是否还在执行
    # thread2.join()
    # print("退出")
    
    # threadLock = threading.Lock()
    # threads=[]
    #
    # # 创建新线程
    # thread1=MyThread2(1, "Thread-1", 1)
    # thread2=MyThread2(2, "Thread-2", 2)
    #
    # # 开启新线程
    # thread1.start()
    # thread2.start()
    #
    # # 添加线程到线程列表
    # threads.append(thread1)
    # threads.append(thread2)
    #
    # # 等待所有线程完成
    # for t in threads:
    #     t.join()
    # print("退出主线程")
    head_time = time.time()
    # run_time_1(3)
    # run_time_2(3)
    threadLock = threading.Lock()
    thread1 = RunThread()
    thread2 = RunThread2()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    last_time = time.time()
    print("时间差is",last_time-head_time)
    """
    直径运行函数，花费6.0ms
    用多线程，花费3.0ms
    用线程同步为6.0ms
    """





