import time
from multiprocessing import Process, Pool


def eat(name):
    for i in range(6):
        print(f'{name}正在吃饭...')
        time.sleep(0.3)

def work():
    for i in range(6):
        print('正在做作业...')
        time.sleep(0.3)

def game():
    for i in range(6):
        print('正在打游戏...')
        time.sleep(0.3)

if __name__ == '__main__':

    process_pool = Pool(2)

    # apply 函数是一个阻塞的函数(主进程阻塞)
    # process_pool.apply(eat,args=('席斌',)) # 从进程池中请求一个新的进程去执行eat
    # process_pool.apply(work)

    # async:异步调用(非阻塞)
    process_pool.apply_async(eat, args=('席斌',))
    process_pool.apply_async (work)
    process_pool.apply_async (game)
    # 表示进程池关闭,进程池不再接受新的请求
    process_pool.close()
    """采用进程池的异步调用,一定要手动的调用join函数
    (因为采用进程池的时候进程池是进程的管理者，主进程不参与管理进程，所以主进程执行到这里如果不调用join会退出)"""
    process_pool.join()
