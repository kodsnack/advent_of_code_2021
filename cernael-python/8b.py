def solve(lines):
    c = 0
    for l in lines:
        l = l.split(' | ')
        digits = l[0].split(' ')
        output = l[1].split(' ')

        dm = {}
        seg = {}
        char = {
            'a': [],
            'b': [],
            'c': [],
            'd': [],
            'e': [],
            'f': [],
            'g': [],
        }
        # find easy digits, map segment occurrences in digits
        for d in digits:
            if len(d) == 2: dm['1']  =  sorted(d)
            elif len(d) == 3: dm['7'] = sorted(d)
            elif len(d) == 4: dm['4'] = sorted(d)
            elif len(d) == 7: dm['8'] = sorted(d)
            for x in d:
                char[x].append(d)

        # map segments
        for k,v in char.items():
            if len(v) == 6:
                seg[k] = 2
                seg[2] = k
            elif len(v) == 4:
                seg[k] = 5
                seg[5] = k
            elif len(v) == 9:
                seg[k] = 6
                seg[6] = k
            elif len(v) == 8:
                if k not in dm['1']:
                    seg[k] = 1
                    seg[1] = k
                else:
                    seg[k] = 3
                    seg[3] = k
            elif len(v) == 7:
                if k  in dm['4']:
                    seg[k] = 4
                    seg[4] = k
                else:
                    seg[k] = 7
                    seg[7] = k
        # find hard digits
        for d in digits:
            if len(d) == 5:
                if seg[2] in d:
                    dm['5']  =  sorted(d)
                elif seg[5] in d:
                    dm['2']  =  sorted(d)
                else:
                    dm['3']  =  sorted(d)
            elif len(d) == 6:
                if seg[3] not in d:
                    dm['6'] = sorted(d)
                elif seg[4] not in d:
                    dm['0'] = sorted(d)
                elif seg[5] not in d:
                    dm['9'] = sorted(d)
        out = []
        for d in output:
            for k,v in dm.items():
                if ''.join(sorted(d)) == ''.join(v): out.append(k)
        c += int(''.join(out))
    return c

if __name__ == '__main__':
    lines = []
    with open('8.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))
