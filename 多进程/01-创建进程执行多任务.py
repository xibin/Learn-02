import time
from multiprocessing import Process


def eat():
    for i in range(6):
        print('正在吃饭...')
        time.sleep(0.3)

def work():
    for i in range(6):
        print('正在做作业...')
        time.sleep(0.3)


if __name__ == '__main__':

    # 创建一个子进程，每个任务由一个独立的子进程来完成
    p1 = Process(target=eat, name='进程1')
    p2 = Process(target=work, name='进程2')

    p1.start()
    p2.start()

    # 主进程自动等待，所有的子进程去执行各自的任务，一直到所有的子进程都结束，主进程才结束