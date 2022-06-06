import requests
import re
import multiprocessing

# Функция обработчик
def hadle(some_value):
    pass

some_List = ['sd', 'asdaa']

# Указываем количество процессов, multiprocessing.cpu_count() - метод для определения количества процессов
with multiprocessing.Pool(2) as process:
    # hadle - метод
    # передает аргументы в список
    process.map(hadle, some_List)