from random import randrange

first = [randrange(100) for i in range(30)]
print(first)
print([j for num, j in enumerate(first[1:]) if j > first[num]])
