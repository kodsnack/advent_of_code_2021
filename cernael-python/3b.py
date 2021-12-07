def find_most_common_bit(lines, bit):
    ones = sum([int(l[bit]) for l in lines])
    zeros = len(lines) - ones
    if ones == zeros: return 'b'
    elif ones > zeros: return '1'
    elif ones < zeros: return '0'

def find_ogr(lines):
    for bit in range(len(lines[0])):
        mcb = find_most_common_bit(lines, bit)
        lines = list(filter((lambda l: l[bit] == mcb or (l[bit] == '1' and mcb =='b')), lines))
        if len(lines) == 1: return int(lines[0],2)

def find_cor(lines):
    for bit in range(len(lines[0])):
        mcb = find_most_common_bit(lines, bit)
        lines = list(filter((lambda l: (l[bit] != mcb and mcb != 'b') or (l[bit] == '0' and mcb =='b')), lines))
        if len(lines) == 1: return int(lines[0],2)

def solve(lines):
    ogr = find_ogr(lines)
    cor = find_cor(lines)

    return ogr * cor

if __name__ == '__main__':
    lines = []
    with open('3.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))

