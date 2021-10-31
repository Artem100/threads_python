import threading
import time


class MyThread(threading.Thread):
# Cоздаем класс с методом который будет запускать потоки

    def run(self):
        # Метод старта потока
        print(f"\nStart thread {self.getName()}")
        try:
            if self._target: # Вызовет функцию target в Thread
                # Функция которая будет выполняться в потоке
                self._target(*self._args, **self._kwargs)
        finally:
            del self._target, self._args, self._kwargs
        print(f"Finished thread {self.getName()}")



def sleeper(n, name):
    print(f'Hi I am {name}, I am going to sleep')
    time.sleep(n)
    print(f'{name} has waked up')

for i in range(4):
    t = MyThread(target=sleeper,
                 name=f"Thread {i+1}",
                 args=(3, 'Vasya'))
    t.start()
