import time
from multiprocessing import Process, Pipe
import multiprocessing
# macos切换fork启动，不会出现SemLock报错
multiprocessing.set_start_method("fork", force=True)


def add_data(pi: Pipe):
    for i in range(6):
        pi.send(f'数据{i}')
        time.sleep(0.3)


def read_data(p1: Pipe):
    while True:
        # recv函数是一个阻塞函数
        value = p1.recv()
        print(value)
        time.sleep(0.4)

if __name__ == '__main__':
    # 创建一个管道，需要两个端点
    send_pipe, recv_pi = Pipe()

    p1 = Process(target=add_data, args=(send_pipe,))
    # 往队列中存放数据
    p2 = Process(target=read_data, args=(recv_pi,))
    # 从队列中读取数据

    p1.start()
    p2.start()

    # 多进程是不能共享变量的
