import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import requests
import time, os


#
# def get_page(url):
#     print('<%s> is getting [%s]' % (os.getpid(), url))
#     response = requests.get(url)
#     if response.status_code == 200:  # 200代表状态：下载成功了
#         return {'url': url, 'text': response.text}
#
#
# def parse_page(res):
#     res = res.result()
#     print('<%s> is getting [%s]' % (os.getpid(), res['text']))
#
#
# if __name__ == '__main__':
#     start_time = time.time()
#     # p = ThreadPoolExecutor()
#     p = ProcessPoolExecutor()
#     l = [
#         'http://www.baidu.com',
#         'http://www.baidu.com',
#         'http://www.baidu.com',
#         'http://www.baidu.com',
#     ]
#     for url in l:
#         p.submit(get_page, url).add_done_callback(parse_page)
#         #  先把返回的res得到一个结果。即在前面加上一个res.result() #谁好了谁去掉回调函数
#         # 回调函数也是一种编程思想。不仅开线程池用，开线程池也用
#     p.shutdown()  # 相当于进程池里的close和join
#     print('主', os.getpid())
#     print('执行结束', time.time() - start_time)
class ThreeTwoOne:
    @classmethod
    async def begin(cls):
        print(3)
        await asyncio.sleep(1)
        print(2)
        await asyncio.sleep(1)
        print(1)
        await asyncio.sleep(1)
        return


async def test():
    await ThreeTwoOne.begin()
    print("test3")


async def game():
    await ThreeTwoOne.begin()
    print('start')


loop = asyncio.get_event_loop()
res = loop.run_until_complete(asyncio.wait([game(), test()]))
loop.close()
