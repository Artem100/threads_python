import threading
import time

def sleeper(n, name):
    for i in range(1, n):
        print(f'Hi I am {name}, I will sleep')
        time.sleep(i)
        print(f'{name} has waked up')


t = threading.Thread(target=sleeper, name='Thread1', args=(5, 'Vasya'))
# name - имя потока,
# В target пишем фунцкцию, args = аргументы для фунции в target

t.start()# Запускаем поток
sleeper(6, "Gena") # Создаем там второй поток для той же функции с другими параметрами
t.join() # ждем завершения даного потока, чтоб перейти на следующю строку кода
print('\nCode after finishing thread')
