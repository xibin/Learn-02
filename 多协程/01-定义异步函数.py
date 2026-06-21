import asyncio
import time


def hello(msg: str):
    print(f'hello {msg}')

async def test1():
    print('hello')
    # 挂起当前的协程，等待1秒钟
    # 当该协程挂起的时候，可以去执行其他的协程(异步任务)
    await asyncio.sleep(1) #目的：切换
    # time.sleep(1) 不会进行协程的切换，只会让当前线程挂起，并且等待1秒钟
    print('world')

# 创建一个协程，但是还没运行
# coroutine = test1()
# print(coroutine)

# 启动协程
asyncio.run(test1())