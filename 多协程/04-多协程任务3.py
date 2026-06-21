import asyncio
import time


async def eat():
    for i in range(6):
        print('正在吃饭...')
        await asyncio.sleep(0)

async def work():
    for i in range(6):
        print('正在做作业...')
        await asyncio.sleep(0)

async def main(): # 其他协程的入口
    task1 = asyncio.create_task(eat())
    task2 = asyncio.create_task(work())

    # await task1
    # await task2
    await asyncio.gather(task1, task2)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)