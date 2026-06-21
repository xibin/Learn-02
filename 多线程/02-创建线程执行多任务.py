import time
from threading import Thread


class EatThread(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        for i in range(6):
            print(f'线程{self.name}:正在吃饭...')
            time.sleep(0.3)

class WorkThread(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        for i in range(6):
            print(f'进程{self.name}:正在做作业...')
            time.sleep(0.3)

if __name__ == '__main__':

    eat = EatThread('t-1')
    work = WorkThread('t-2')

    eat.start()
    work.start()