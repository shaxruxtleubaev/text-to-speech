import random

a = [1, 2, 3]

b = random.randint(0, len(a)-1)

a.insert(b, 5)
a.remove(b+1)
print(a)