import random


class RandomQueue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def is_full(self): #kolejka nigdy nie jest pełna
        return False

    def insert(self, item):    # wstawia element w czasie O(1)
        if self.is_full():
            raise ValueError("The queue is full!")

        self.items.append(item)

    def remove(self):  # zwraca losowy element w czasie O(1)
        if self.is_empty():
            raise ValueError("The queue is empty!")

        x = random.randrange(len(self.items))
        self.items[x], self.items[-1] = self.items[-1], self.items[x]

        return self.items.pop()

    def clear(self):   # czyszczenie listy
        self.items = []







