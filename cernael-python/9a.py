def solve(lines):
    map = [[int(c) for c in l] for l in lines]
    lows = [
             [
               map[i][j] + 1
                 if
                   (i == 0 or map[i][j] < map[ i - 1 ][ j ]) and
                   (j == 0 or map[i][j] < map[ i ][ j - 1 ]) and
                   (i == len(map)-1 or map[i][j] < map[ i + 1 ][ j ]) and
                   (j == len(map[0])-1 or map[i][j] < map[ i ][ j + 1 ])
                 else 0
                 for j in range(len(map[i]))
             ] for i in range(len(map))
           ]
    return sum([sum(l) for l in lows])


if __name__ == '__main__':
    lines = []
    with open('9.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))
