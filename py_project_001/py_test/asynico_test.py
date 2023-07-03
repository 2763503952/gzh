"""Python的异步"""
import requests,logging
import asyncio,aiohttp
import time


url = 'https://httpbin.org/delay/5'

def decorator_time(fnc):
    """
    时间装饰器
    :return: function
    """
    def inner():
        start_time = time.time()
        fnc()
        end_time = time.time()
        print("所需时间为：",end_time-start_time)

    return inner

@decorator_time
def ay_spider():
    """
    异步爬虫
    """
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s: %(message)s')
    for _ in range(5):
        logging.info('scraping %s',url)
        response = requests.get(url=url)

async def excute(x):
    """
    async关键字，声明一个携程方法
    """
    print('Number:',x)


async def request():
    #请求百度方法，returns:response对象
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status


def call_back(task):
    #定义回调函数
    print("调用回调函数，结果为;",task.result())


def user_request():
    #使用协程
    coroutine = request()
    loop = asyncio
    task = asyncio.ensure_future(coroutine,loop=loop)
    task.add_done_callback(call_back)
    loop.run_until_complete(task)





def user_async():
    """
    调用协程方法
    :return:
    """
    coroutine = excute(1)
    print(coroutine) #<coroutine object excute at 0x000002228E1CA3C8>

    loop = asyncio.get_event_loop()#定义任务循环对象
    print("loop:",loop)
    task = loop.create_task(coroutine)#把coroutine打包成task（任务）
    # task = asyncio.ensure_future(coroutine) #与上述效果相同
    print("Task:",task)#running
    loop.run_until_complete(task)#循环执行task（任务）
    print("Task:",task)#done





if __name__ == '__main__':
    # ay_spider() #所需时间120s
    # user_async()
    user_request()


