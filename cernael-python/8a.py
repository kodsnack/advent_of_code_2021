def solve(lines):
    c = 0
    for l in lines:
        l = l.split(' | ')
        digits = l[0].split(' ')
        output = l[1].split(' ')
        print('line:',l)
        for d in output:
            ld = len(d)
            if ld == 2 or ld == 4 or ld == 3 or ld == 7:
                print(d,ld)
                c += 1
    return c

if __name__ == '__main__':
    lines = []
    with open('8.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))
