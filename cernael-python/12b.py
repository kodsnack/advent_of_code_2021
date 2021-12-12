def solve(lines):
    edges = {}
    for l in lines:
        a,b = l.split('-')
        if a in edges:
            edges[a].append(b)
        else:
            edges[a] = [b]
        if b in edges:
            edges[b].append(a)
        else:
            edges[b] = [a]

    paths = set()
    pps = [[True,'start',a] for a in edges['start']]
    while pps:
        e = pps.pop()
        next = [e + [a] for a in edges[ e[-1] ] ]
        for p in next:
            if p[-1] == 'end':
                paths.add(tuple(p[1:]))
            elif p[-1] == 'start':
                pass
            elif p[-1].isupper():
                pps.append(p)
            elif p.count(p[-1]) == 1 :
                pps.append(p)
            elif p.count(p[-1]) == 2 and p[0]:
                pps.append([False]+p[1:])
    return len(paths)

if __name__ == '__main__':
    lines = []
    with open('12.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))
