from collections import deque

lines = open('input.txt').read().splitlines()
lines = [int(line) for line in lines]

p1 = 0
for a,b in zip(lines, lines[1:]):
    p1 += b > a  
print(p1)

p2 = 0
window = deque()
window.append(lines[0])
window.append(lines[1])
window.append(lines[2])
previous = sum(window)

for new in lines[3:]:
    window.popleft()
    window.append(new)
    current = sum(window)

    if current > previous:
        p2 += 1
    previous = current
print(p2)