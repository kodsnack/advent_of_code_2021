from common import getPuzzle, submitSecure

puzzle = getPuzzle()

inp = puzzle.input_data
ds = [int(s) for s in inp.splitlines()]
parta = sum(map(lambda x, y:x<y, ds[:-1], ds[1:]))
d3s = [ds[i:i+3] for i in range(len(ds)-2)]
partb = sum(map(lambda x, y:sum(x)<sum(y), d3s[:-1], d3s[1:]))

submitSecure(puzzle, "a", parta)
submitSecure(puzzle, "b", partb)
