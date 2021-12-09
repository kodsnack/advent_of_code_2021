def solve(lines):
    nums = lines.pop(0).split(',')
    boards = [[r.split() for r in lines[6*n+1:6*n+6]] for n in range(int(len(lines)/6))]

    # boards is now a grid/row/column 3D array
    for num in nums:
        boards = mark_nums(boards, num)
        while True:
            winner = check_win(boards)
            if winner != -1:
                if len(boards) > 1:
                    boards.pop(winner)
                else:
                    return count_score(boards[winner]) * int(num)
            else: break
    for b in boards[:8]: print(b)

def mark_nums(boards, num):
    return [[[c if c != num else '' for c in l] for l in b] for b in boards]

def check_win(boards):
    for ix in range(len(boards)):
        b = boards[ix]
        for l in b:
            if ''.join(l) == '':
                return ix
        b = [[b[j][i] for j in range(len(b[0]))] for i in range(len(b))]
        for l in b:
            if ''.join(l) == '':
                return ix
    return -1

def count_score(board):
    return sum([sum([int(a) if a != '' else 0 for a in l]) for l in board])

if __name__ == '__main__':
    lines = []
    with open('4.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))
