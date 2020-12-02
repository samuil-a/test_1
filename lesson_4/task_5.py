from functools import reduce

first = [i for i in range(100, 1001) if i % 20 == 0 or i % 21 == 0]
print(first)
print(reduce(lambda x, y: x * y, first))
