import itertools
import random

count = 0
x = 12  #ustawiam wartosc x, aby nie tworzyc petli nieskonczonej - pomijam gdy chce uzyskać wartość nieskończona
# printuje iteratory, aby sprawdzic ich dzialanie

iter_one = itertools.cycle('AB')

while True:
    print(next(iter_one), end = ' ')
    count += 1
    if count == x:
        break
##########
myList= ["N", "E", "S", "W"]
iter_two = iter(lambda: random.choice(myList), -1)

count = 0
print('\n')
while True:
    print(next(iter_two), end = ' ')
    count +=1
    if count == x:
        break

# ###########
iter_three = itertools.cycle(range(7))
count = 0
print('\n')

while True:
    print(next(iter_three), end = ' ')
    count +=1
    if count == x:
        break
