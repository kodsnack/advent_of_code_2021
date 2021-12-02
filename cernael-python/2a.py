def solve(lines):
    pos, dep = 0,0
    for l in lines:
        if l[0] == 'forward': pos += int(l[1])
        elif l[0] == 'down': dep += int(l[1])
        elif l[0] == 'up': dep -= int(l[1])

    return dep * pos

if __name__ == '__main__':
    lines = []
    with open('2.txt') as f:
        for line in f.readlines():
            lines.append(line.split())
    print(solve(lines))
