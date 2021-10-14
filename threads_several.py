from threading import *
from time import time, sleep

def one(num):
    sleep(num)

def two(num):
    sleep(num)

t1 = Thread(target=one, args=(1,)) # Создаем поток и в target засовываем нужную фунцкцию, args = аргументы для фунции в target
t2 = Thread(target=two, args=(1,))



x1 = time() # Засекем

t1.start() # Запускаем поток
t2.start()

t1.join()# ждем завершения даного потока, чтоб перейти на следующю строку кода
t2.join()

x2 = time() # Фиксируем время время

print(x2-x1)