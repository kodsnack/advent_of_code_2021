def solve(lines):
    lines = map(int, lines)
    count, win = 0, []
    for i in lines:
        win.append(i)
        if len(win) == 4:
            count += 1 if win[0] < win[-1] else 0
            win.pop(0)

    return count

if __name__ == '__main__':
    lines = []
    with open('1.txt') as f:
        for line in f.readlines():
            lines.append(line)
    print(solve(lines))
