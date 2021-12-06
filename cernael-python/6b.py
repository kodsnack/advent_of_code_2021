def solve(lines):
    l = lines[0].split(',')
    daycounts = [0] * 9
    for f in l:
        daycounts[int(f)] += 1
    for d in range(256):
        c = daycounts.pop(0)
        daycounts[6] += c
        daycounts.append(c)
    return sum(daycounts)

if __name__ == '__main__':
    lines = []
    with open('6.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))

