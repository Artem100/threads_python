import threading
import time


class MyThread(threading.Thread):
# Cоздаем класс с методом c контркутором
    def __init__(self, number, func, args):
        threading.Thread.__init__(self)
        self.number = number # Номер потока, чтоб было видно в print
        self.func = func
        self.args = args

    def run(self):
        # Метод старта потока
        print(f"Start thread {self.number}")
        self.func(*self.args)
        print(f"Finished thread {self.number}")

def double(number, cycles):
    for i in range (cycles):
        number +=number
    print(number)

thread_list = [] # В список помещаем потоки, чтоб затем вытащить поток и останить его процесс

for i in range(50):
    t = MyThread(number=i+1, func=double, args=[i, 3])
    thread_list.append(t)
    t.start()

for t in thread_list:
    t.join()




