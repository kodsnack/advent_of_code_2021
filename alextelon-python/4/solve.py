# First special line manually copied over here and removed from input file.
nums = '18,99,39,89,0,40,52,72,61,77,69,51,30,83,20,65,93,88,29,22,14,82,53,41,76,79,46,78,56,57,24,36,38,11,50,1,19,26,70,4,54,3,84,33,15,21,9,58,64,85,10,66,17,43,31,27,2,5,95,96,16,97,12,34,74,67,86,23,49,8,59,45,68,91,25,48,13,28,81,94,92,42,7,37,75,32,6,60,63,35,62,98,90,47,87,73,44,71,55,80'
nums = list(map(int,nums.split(',')))

# Find all grids.
grids = []
for board in open('input.txt').read().split('\n\n'):
    grid = []
    for line in board.splitlines():
        row = list(map(int, line.split()))
        grid.append(row)

    grids.append(grid)


def has_won(grid, called_out):
    # There are two ways to get bingo. Rows and cols.
    rows = grid
    cols = zip(*grid)

    candidates = rows
    candidates.extend(cols)

    for line in candidates:
        if all(x in called_out for x in line):
            return True
    return False

def nums_not_called_out(grid, called_out):
    # The final score is calculated by counting the sum of the numbers not called out yet.
    all_nums = set()
    for row in grid:
        for x in row:
            all_nums.add(x)
    
    return sum(all_nums - set(called_out))

n = len(grids)

called_out = []
for i, num in enumerate(nums):
    called_out.append(num)
    for grid in grids:
        if has_won(grid, called_out):
            grids.remove(grid)
            # p1 would exit and print here!

        if len(grids) == 0:
            # We have removed the last grid. so print this one.
            print(num * nums_not_called_out(grid, called_out))
            exit()