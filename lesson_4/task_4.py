from random import randrange

first = [randrange(1, 10) for i in range(20)]
print(first)
print([i for i in first if first.count(i) == 1])
