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

# oxygen rating most common value in current bit position. bias to 1
# scrubber the other way around. least common. bias to 0.

# oxygen:
data = lines[::]
for i in range(len(data[0])):
    # Take the bits from the i'th column of the data that is left.
    bits = list(zip(*data))[i]
    if len(data) == 1:
        break
    if bits.count('0') > bits.count('1'):
        data = [line for line in data if line[i] == '0']
    else:
        data = [line for line in data if line[i] == '1']
if len(data) == 1:
    oxygen = data[0]
oxygen = int(oxygen, 2)

# co2:
data = lines[::]
for i in range(len(data[0])):
    # Take the bits from the i'th column of the data that is left.
    bits = list(zip(*data))[i]
    if len(data) == 1:
        break
    if bits.count('0') <= bits.count('1'):
        data = [line for line in data if line[i] == '0']
    else:
        data = [line for line in data if line[i] == '1']
if len(data) == 1:
    co2 = data[0]
co2 = int(co2, 2)
print('p2', co2*oxygen)