from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(enhancement, image, steps=2):
    height = len(image)
    width = len(image[0])

    new_image = []

    for _ in range(steps):
        new_image.append(''.join(['.' for _ in range(width + steps*2)]))

    for row in image:
        new_image.append(''.join(['.' for _ in range(steps*1)] + list(row) + ['.' for _ in range(width*1)]))

    for _ in range(steps):
        new_image.append(''.join(['.' for _ in range(width + steps*4)]))

    image = new_image
    height = len(image)
    width = len(image[0])

    def pixel(image, y, x, step):
        if y < 0 or x < 0 or y == height or x == width:
            if step % 2 == 0 :
                return '.'
            return '#'
        return image[y][x]

    def process(image, y, x, step):
        window = ''

        for dy in range(y-1,y+2):
            for dx in range(x-1,x+2):
                window += pixel(image, dy, dx, step)

        window = window.replace('.', '0')
        window = window.replace('#', '1')

        val = int(window, 2)
        return enhancement[val]
    
    def enhance(image, step):
        new_image = []        

        for y in range(height):
            new_row = []
            for x in range(width):
                new_row.append(process(image, y, x, step))
            new_image.append(new_row)

        return new_image

    def c():
        count = 0

        for line in image:
            count += line.count('#')

        return count


    for step in range(steps): 
        image = enhance(image, step)
    
    return c()


def main():
    enhancement = ''
    image = []

    with open('20.txt') as f:
        for line in f.readlines():
            if not enhancement:
                enhancement = line.rstrip()
            elif line.rstrip():
                image.append(line.rstrip())
            
    return solve(enhancement, image)


if __name__ == '__main__':
    print(main())