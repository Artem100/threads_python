import threading
import time

"""
Здесь создаем неупорядоченные список потоков

"""

def sleeper(n, name):
    print(f'Hi I am {name}, I am going to Start')
    time.sleep(n)
    print(f'{name} has stop')


t = threading.Thread(target=sleeper, name='Thread optional', args=(5, 'Vasya'))
# name - имя потока,
# Создаем поток и в target засовываем нужную фунцкцию, args = аргументы для фунции в target

thread_list = []

start = time.time()

for i in range(5):
    t = threading.Thread(target=sleeper,
                         name=f'Thread{i}',
                         args=(5, f'Thread{i}'))
    thread_list.append(t)
    t.start()
    print(f"{t.name} has started")

for t in thread_list:
    t.join()

end = time.time()

print(f"Full time {end-start}")

print("All threads done")