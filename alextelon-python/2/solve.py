lines = open('input.txt').read().splitlines()
horizontal = 0
depth = 0
aim = 0

for line in lines:
    command, num = line.split(' ')
    num = int(num)

    if command == 'forward':
        horizontal += num
        depth += aim * num
    elif command == 'up':
        aim -= num
    elif command == 'down':
        aim += num

print(horizontal * depth)