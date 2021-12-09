def solve(lines):
    l = [int(i) for i in lines[0].split(',')]
    tries = {}
    for p in range(min(l), max(l)):
        tries[p] = sum([abs(p-i)*(abs(p-i)+1)/2 for i in l])
    return min(tries.values())

if __name__ == '__main__':
    lines = []
    with open('7.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))
