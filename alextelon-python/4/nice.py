class Grid():
    def __init__(self, grid):
        # There are two ways to get bingo. Rows and cols.
        rows = grid
        cols = list(zip(*grid))
        self.candidates = [set(candidate) for candidate in rows + cols]

        self.all_nums = set()
        for row in grid:
            self.all_nums.update(row)

    def bingo(self, called_out):
        # If a line (row or col) is a subset of the numbers called -> BINGO!
        return any(line <= called_out for line in self.candidates)

    def score(self, called_out):
        return sum(self.all_nums - called_out)


nums, *boards = open('input.txt').read().split('\n\n')
nums = [int(num) for num in nums.split(',')]

# Find all grids.
grids = []
for board in boards:
    grid = []
    for line in board.splitlines():
        grid.append([int(x) for x in line.split()])
    grids.append(Grid(grid))

called_out = set()
for num in nums:
    called_out.add(num)

    for grid in grids:
        if grid.bingo(called_out):
            grids.remove(grid)
            # (p1 would exit and print here!)

        if len(grids) == 0:
            # We have removed the last grid. so print this one.
            print(num * grid.score(called_out))
            exit()