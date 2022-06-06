import random
from threading import Thread
from collections import defaultdict

what_list = ['a', 'v', 'c', '2', '3', '4', '7']

class WhatTake(Thread):

    def __init__(self, name, some_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.some_list = some_list
        self.catch = defaultdict(int)

    def run(self):
        self.catch = defaultdict(int)
        for i in range(1, 3):
            value = random.choice(self.some_list)
            print(f"{self.name}: {value}")
            self.catch[value] += 1

vasya = WhatTake(name='Гена', some_list=what_list)
kolya = WhatTake(name='Чешир', some_list=what_list)


vasya.start()
kolya.start()

vasya.join()
kolya.join()

print("Закончили")

for asdasd in (vasya, kolya):
    print(f'Итого буквы {asdasd.name}:')
    for fish, count in asdasd.catch.items():
        print(f'    {fish} - {count}')