def solve(lines):
    bits = [int(c) for c in lines[0]]
    for l in lines[1:]:
        for i in range(len(l)):
            bits[i] += int(l[i])
    gamma = int(''.join([str(1) if bit>len(lines)/2 else str(0) for bit in bits]),2)
    epsilon = int(''.join([str(1) if bit<len(lines)/2 else str(0) for bit in bits]),2)
    return gamma * epsilon
if __name__ == '__main__':
    lines = []
    with open('3.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))
