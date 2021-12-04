lines = open('input.txt').read().splitlines()
lines = [int(line) for line in lines]

print(sum(b > a for a,b in zip(lines, lines[1:])))

# This solution for p2 uses inspiration from r/adventofcode which had some nice solutions like this.
# Now compare against a running average. Use zip again to create a window into the data of size 3
windows = [sum(window) for window in zip(lines, lines[1:], lines[2:])]

# Same code as p1. But now we compare the windows to eachother instead.
print(sum(b > a for a,b in zip(windows, windows[1:])))
