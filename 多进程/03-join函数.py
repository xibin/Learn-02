import time
from multiprocessing import Process


class EatProcess(Process):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        for i in range(6):
            print(f'进程{self.name}:正在吃饭...')
            time.sleep(0.3)

class WorkProcess(Process):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        for i in range(6):
            print(f'进程{self.name}:正在做作业...')
            time.sleep(0.3)

if __name__ == '__main__':

    eat = EatProcess('process=01')
    work = WorkProcess('process=02')

    eat.start()
    # 子进程可以调用join函数
    # 要在start后调用join
    eat.join()

    work.start()
