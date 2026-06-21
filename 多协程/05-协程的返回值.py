import asyncio
import time


async def eat():
    for i in range(6):
        print('正在吃饭...')
        await asyncio.sleep(0)
    return '吃饭完成'

async def work():
    for i in range(6):
        print('正在做作业...')
        await asyncio.sleep(0)
    return '做作业完成'

async def main(): # 其他协程的入口
    task1 = asyncio.create_task(eat())
    task2 = asyncio.create_task(work())
    task1.cancel()

    # await task1
    # await task2
    # 仅仅得到函数的返回值
    # result = await asyncio.gather(task1, task2) # 当第一个协程强制终止了，会影响第二个协程
    result = await asyncio.gather(task1, task2, return_exceptions=True)
    # 得到更加详细返回内容
    # result = await asyncio.wait([task1, task2],return_when=asyncio.ALL_COMPLETED)
    # result = await asyncio.wait([task1, task2])
    print(result)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)