lines = open('input.txt').read().splitlines()
gamma = ""
eps = ""

for x in zip(*lines):
    if x.count('0') > x.count('1'):
        gamma += '0'
        eps += '1'
    else:
        gamma += '1'
        eps += '0'

g = int(gamma, 2)
e = int(eps, 2)
print('p1', e*g)

def cols(rows):
    return zip(*rows)

def rule(rows, f):
    for i in range(len(rows[0])):
        # Take the bits from the i'th column of the data that is left.
        bits = list(cols(rows))[i]
        rows = [row for row in rows if row[i] == f(bits)]
        if len(rows) == 1:
            break
    else:
        raise Exception('More than 1 data left after filtering out')

    return int(rows[0], 2)

def get_oxygen(data):
    most_common = lambda bits: '1' if bits.count('1') >= len(bits) // 2 else '0'
    return rule(data, most_common)

def get_co2(data):
    least_common = lambda bits: '0' if bits.count('1') >= len(bits) // 2 else '1'
    return rule(data, least_common)

oxygen = get_oxygen(lines)
co2 = get_co2(lines)
print('p2', co2*oxygen)