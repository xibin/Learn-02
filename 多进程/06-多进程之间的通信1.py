import time
from multiprocessing import Process, Pool, Queue
import multiprocessing
# macos切换fork启动，不会出现SemLock报错
multiprocessing.set_start_method("fork", force=True)


def add_data(q: Queue):
    for i in range(6):
        q.put(f'数据{i}')
        time.sleep(0.3)


def read_data(q: Queue):
    while True:
        # get函数是个阻塞的函数，get从队列中获取一个值，并且这个值从队列中删除。
        value = q.get()
        print(value)
        time.sleep(0.4)

if __name__ == '__main__':

    q = Queue(100)

    p1 = Process(target=add_data, args=(q,))
    # 往队列中存放数据
    p2 = Process(target=read_data, args=(q,))
    # 从队列中读取数据

    p1.start()
    p2.start()

    # 多进程是不能共享变量的
