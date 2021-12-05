from collections import Counter
from typing import Iterable
from itertools import product

# I guess I will create my own aoc lib and add this as my first helper function.
def my_range(a:int, b:int) -> Iterable:
    """Inclusive both ends, handles positive and negative direction.
    
    Example:
     my_range(3, 0) -> 3, 2, 1, 0
     my_range(0, 3) -> 0, 1, 2, 3
    """
    if a > b: 
        yield from range(a, b-1, -1)
    yield from range(a, b+1)

# New format: x,y,xx,yy
data = open('input.txt').read().replace('->', ',')

count = Counter()
for line in data.splitlines():
    x, y, xx, yy = map(int, line.split(','))

    diagonal = abs(xx - x) == abs(yy - y)
    axial = x == xx or y == yy

    if diagonal:
        count.update(zip(my_range(x, xx), my_range(y, yy)))
    elif axial:
        count.update(product(my_range(x, xx), my_range(y, yy)))

print(sum(v>1 for v in count.values()))