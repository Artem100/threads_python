import threading
import time

total = 4

def create_item():
    global total
    # В каждой итерации будем делать изменения глобальной переменной total
    for i in range(3):
        time.sleep(2)
        print(f'iteration first method {i}')
        total +=1
    print('iterations finished')

def create_items_2():
    global total
    # В каждой итерации будем делать изменения глобальной переменной total
    for i in range(3):
        time.sleep(1)
        print(f'\niteration second method {i}')
        total += 1
    print('iterations finished')

# Будет контролировать лимт глобальной переменной total
def limits_items():
    global total
    while True:
        if total > 5:
            print('overloaded')
            total -=3
            print('subtracted by 3')
        else:
            time.sleep(1)
            print('Waiting')

create1 = threading.Thread(target=create_item)
create2 = threading.Thread(target=create_items_2)
limiter = threading.Thread(target=limits_items, daemon=True)
# Daemaon - значит что поток остановиться, когда все потоки остальные перестанут работать

create1.start()
create2.start()
limiter.start()

create1.join()
create2.join()
# limiter.join()

print("Finish all")