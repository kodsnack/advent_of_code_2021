def solve(lines):
    nums = lines.pop(0).split(',')
    boards = [[r.split() for r in lines[6*n+1:6*n+6]] for n in range(int(len(lines)/6))]

    # boards is now a grid/row/column 3D array
    for num in nums:
        boards = mark_nums(boards, num)
        winscore = check_win(boards)
        if winscore != -1:
            return winscore * int(num)

def mark_nums(boards, num):
    return [[[c if c != num else '' for c in l] for l in b] for b in boards]

def check_win(boards):
    for b in boards:
        win = False
        for l in b:
            if ''.join(l) == '':
                win = True
        b = [[b[j][i] for j in range(len(b[0]))] for i in range(len(b))]
        for l in b:
            if ''.join(l) == '':
                win = True
        if win:
             return sum([sum([int(a) if a != '' else 0 for a in l]) for l in b])
    return -1

if __name__ == '__main__':
    lines = []
    with open('4.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))
