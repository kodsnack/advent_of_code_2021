from  functools import *

def countinc(a, b):
    return 1 if a < b else 0

def solve(lines):
    lines = map(int, lines)
    count, old, new = 0, None, None
    for i in lines:
        old = new
        new = i
        if old != None:
            count += countinc(old, new)

#reduce(countinc, lines, 0)
    return count

if __name__ == '__main__':
    lines = []
    with open('1.txt') as f:
        for line in f.readlines():
            lines.append(line)
    print(solve(lines))
