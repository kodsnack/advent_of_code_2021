def solve(lines):
    points, p = {}, []
    for l in lines:
        x1, y1, x2, y2 = [int(i) for i in l.replace(' -> ', ',').split(',')]
        if y1 == y2:
            if x1 < x2:
                # hor, asc
                p = [(r, y2) for r in  range(x1,x2 + 1)]
            else:
                # hor, desc
                p = [(r, y2) for r in  range(x2,x1 + 1)]
        elif x1 == x2:
            if y1 > y2:
                # ver, desc
                p = [(x1, r) for r in  range(y2,y1 + 1)]
            else:
                # ver, asc
                p = [(x1, r) for r in  range(y1,y2 + 1)]
        for i in p:
           if i in points.keys():
               points[i] += 1
           else:
               points[i] = 1
        p = []
    return len(list(filter(lambda x: x >= 2, points.values())))

if __name__ == '__main__':
    lines = []
    with open('5.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))
