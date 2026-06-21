import time
from threading import Lock, Thread, current_thread

lock = Lock()
my_list=[1,2,6,8,19]
# 需求：根据下标在列表中取值，保证同一时刻只能有一个线程取值

# def get_value(index):
#     lock.acquire()
#     print(f'当前线程是:{current_thread()}')
#     #判断下标是否越界
#     if(index >= len(my_list)):
#         print(f'下标越界了，你传入的下标是:{index}')
#         lock.release()
#         return
#     v = my_list[index]
#     print(f'当前线程取到的值{v}')
#     time.sleep(0.4)
#     lock.release()

def get_value(index):
    with lock:
        print(f'当前线程是:{current_thread()}')
        #判断下标是否越界
        if(index >= len(my_list)):
            print(f'下标越界了，你传入的下标是:{index}')
            return
        v = my_list[index]
        print(f'当前线程取到的值{v}')
        time.sleep(0.4)


if __name__ == '__main__':
    # 创建二十个线程来模拟多线程分别从列表中取值操作

    for i in range(20):
        t = Thread(target=get_value, args=(i,))
        t.start()
