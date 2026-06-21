import time
from threading import Thread

# 采用两个线程，累加5亿次

def add(n):
    """
    把1累加多少次
    :param n:
    :return:
    """
    sum = 0
    while sum < n:
        sum += 1
    print(f'当前线程加了{sum}次')

if __name__ == '__main__':
    start = time.time()
    n = 500000000

    t1 = Thread(target=add, args=(n/2,), daemon=True)
    t2 = Thread(target=add, args=(n/2,), daemon=True)
    # t1.daemon = True

    t1.start()
    t2.start()
    # t1.join()
    # t2.join()
    # add(n)
    end = time.time()
    print(f'运行的时间为{end - start}')