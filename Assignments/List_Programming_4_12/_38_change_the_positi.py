# Change the position of every nth value with (n+1)th value
from itertools import zip_longest, chain, tee
def replace2copy(n):
    lst1, lst2 = tee(iter(n), 2)
    return list(chain.from_iterable(zip_longest(n[1::2], n[::2])))
n = [0,1,2,3,4,5]
print(replace2copy(n))