def solve(lines):
    points, p = {}, []
    for l in lines:
        x1, y1, x2, y2 = [int(i) for i in l.replace(' -> ', ',').split(',')]
        if y1 == y2:
            if x1 < x2:
                # hor, asc
                p = [(x, y1) for x in  range(x1, x2 + 1)]
            else:
                # hor, desc
                p = [(x, y1) for x in  range(x2, x1 + 1)]
        elif x1 == x2:
            if y1 > y2:
                # ver, desc
                p = [(x1, y) for y in  range(y2, y1 + 1)]
            else:
                # ver, asc
                p = [(x1, y) for y in  range(y1, y2 + 1)]
        elif abs(x1 - x2) == abs(y1 - y2):
            # diag
            if x1 - x2 == y1 - y2:
                # k = 1
                if x1 < x2:
                    # asc
                    p = zip(range(x1, x2 + 1), range(y1, y2 + 1))
                else:
                    # desc
                    p = zip(range(x2, x1 + 1), range(y2, y1 + 1))
            else:
                # k = -1
                if x1 < x2:
                    # x_asc
                    p = zip(range(x1, x2 + 1), range(y1, y2 - 1, -1))
                else:
                    # x_desc
                    p = zip(range(x1, x2 - 1, -1), range(y1, y2 + 1))
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
