import threading
import time

def sleeper(n, name):
    print(f'Hi I am {name}, I will sleep')
    time.sleep(n)
    print(f'{name} has waked up')


t = threading.Thread(target=sleeper, name='Thread1', args=(5, 'Vasya')) # name - имя потока, # Создаем поток и в target засовываем нужную фунцкцию, args = аргументы для фунции в target

t.start()# Запускаем поток
t.join() # ждем завершения даного потока, чтоб перейти на следующю строку кода
print('\nCode after finishing thread')
