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
    await asyncio.gather(eat(), work())

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)