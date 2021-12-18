def solve(lines):
    map = [[int(c) for c in l] for l in lines]
    flashes = 0
    time = 0
    while True:
        time += 1
        map = [[c+1 for c in l] for l in map]
        flashed = set()
        cont = True
        while cont:
            cont = False
            for i in range(len(map)):
                for j in range(len(map[0])):
                    if map[i][j] > 9 and (i,j) not in flashed:
                        flashed.add((i,j))
                        cont = True
                        for p in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                            x, y = i + p[0], j + p[1]
                            if 0 <= x < len(map) and 0 <= y < len(map[0]): map[x][y] += 1
        for f in flashed:
            map[f[0]][f[1]] = 0
        if len(flashed) == 100:
            return time

if __name__ == '__main__':
    lines = []
    with open('11.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))
