import threading


l = threading.Lock() # Гарантирует целостность и поочередность дострупа к глобальной переменной

x = 0
COUNT = 10000

def adding_2():
    global x
    with l:
        for i in range(COUNT):
            x += 2

def adding_3():
    global x
    with l:
        for i in range(COUNT):
            x += 3

def substract_4():
    global x
    with l:
        for i in range(COUNT):
            x -= 4

def substract_1():
    global x
    with l:
        for i in range(COUNT):
            x -= 1


for i in range(COUNT):
    t1 = threading.Thread(target=adding_2)
    t2 = threading.Thread(target=adding_3)
    t3 = threading.Thread(target=substract_4)
    t4 = threading.Thread(target=substract_1)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    if x!=0:
        print(x)
        break

print(x)

