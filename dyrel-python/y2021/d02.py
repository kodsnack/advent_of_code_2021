from common import getPuzzle, submitSecure
from itertools import accumulate

puzzle = getPuzzle()

inp = puzzle.input_data

direction = {"up": -1j, "down": 1j, "forward": 1}

interp = [direction[item[0]] * int(item[1]) 
          for item in (x.split() for x in inp.splitlines())]
part1 = sum(interp)
part2 = sum(map(lambda x,y:x.real+1j*(y*x.real),
                interp, 
                accumulate(map(lambda x:x.imag, interp))))

submitSecure(puzzle, "a", round(part1.real*part1.imag))

submitSecure(puzzle, "b", round(part2.real*part2.imag))
