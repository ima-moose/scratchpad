import random
i = 1
while i <= 100:
    r = random.randint(-5, 5)
    i = i + r
    print(i, r)
    if i <= -100:
        i = 100
