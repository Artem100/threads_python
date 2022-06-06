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
        try:
            self.catch = defaultdict(int)
            for i in range(1, 8):
                value = random.choice(self.some_list)
                if value == '7':
                    print("It was 7")
                    raise ValueError
                print(f"{self.name}: {value}")
                self.catch[value] += 1
        except:
            print("was error")

vasya = WhatTake(name='Гена', some_list=what_list)

vasya.start()
kolya = WhatTake(name='Чешир', some_list=what_list)
kolya.start()
vasya.join()
kolya.join()

print("Закончили")

for result in (vasya, kolya):
    print(f'Итого буквы {result.name}:')
    for fish, count in result.catch.items():
        print(f'    {fish} - {count}')