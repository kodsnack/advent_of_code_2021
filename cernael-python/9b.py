def solve(lines):
    map = [[int(c) for c in l] for l in lines]
    lows = [
             [
               (i,j)
                 for j in range(len(map[i]))
                   if
                     (j == 0 or map[i][j] < map[ i ][ j - 1 ]) and
                     (j == len(map[0])-1 or map[i][j] < map[ i ][ j + 1 ]) and
                     (i == 0 or map[i][j] < map[ i - 1 ][ j ]) and
                     (i == len(map)-1 or map[i][j] < map[ i + 1 ][ j ])
             ] for i in range(len(map))
           ]
    basins = set()
    for low in [item for l in lows for item in l]:
        basin = set()
        border = set()
        test = [low]
        while test:
            t = test.pop()
            if map[t[0]][t[1]] != 9:
                basin.add(t)
                for n in [(t[0]+1,t[1]) , (t[0]-1,t[1]) , (t[0],t[1]+1) , (t[0],t[1]-1)]:
                    if (0 <= n[0] < len(map) and
                       0 <= n[1] < len(map[0]) and
                       n not in basin and n not in border):
                        test.append(n)
            else:
                border.add(t)
        basins.add(frozenset(basin))
    res = [len(s) for s in basins]
    res.sort()
    res.reverse()
    return res[0] * res[1] * res[2]

if __name__ == '__main__':
    lines = []
    with open('9.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))
