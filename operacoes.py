"""Operator"""
from operator import add, mul, sub
from functools import reduce



print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
print(reduce(lambda x, y: x - y, [1, 2, 3, 4,  5]))

# ou, de forma mais legível

print(reduce(add, [1, 2, 3, 4, 5]))
print(reduce(sub, [1, 2, 3, 4, 5]))

