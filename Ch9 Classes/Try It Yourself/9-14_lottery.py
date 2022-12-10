import random

ran = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 'a', 's', 'l', 'w', 'm']

b = 0
while True:
    b += 1
    print(random.choice(ran))
    if b == random.choice(ran):
        break