from common import getPuzzle, submitSecure

NEIGHBOUR9 = (-1-1j, -1j, 1-1j, -1, 0, 1, -1+1j, 1j, 1+1j)

puzzle = getPuzzle()

rawInput = puzzle.input_data

def parseInput(inp):
    l = inp.splitlines()
    ie = dict()
    for i, c in enumerate(l[0]):
        ie[i] = c
    d = dict()
    d['rest'] = '.'
    height, width = 0, 0
    for ri, row in enumerate(l[2:]):
        height = max(height, ri)
        for ci, c in enumerate(row):
            d[ci + 1j*ri] = c
            width = max(width, ci)
    return ie, d, 0, width, 0, height

def enhance(img, imgEn, mic, mac, mir, mar):
    d = dict()
    for r in range(mir-2, mar+3):
        for c in range(mic-2, mac+3):
            p = c+1j*r
            idx = 0
            for delta in NEIGHBOUR9:
                if img.get(p+delta, img['rest']) == '#':
                    idx = idx * 2 + 1
                else:
                    idx = idx * 2
            d[p] = imgEn[idx]
    if img['rest'] == '#':
        d['rest'] = imgEn[511]
    else:
        d['rest'] = imgEn[0]
    return d, mic-2, mac+2, mir-2, mar+2

def countImg(img):
    return ''.join(img.values()).count('#')

imgEn, img, mic, mac, mir, mar = parseInput(rawInput)
for i in range(2):
    img, mic, mac, mir, mar = enhance(img, imgEn, mic, mac, mir, mar)
submitSecure(puzzle, "a", countImg(img))
for i in range(48):
    img, mic, mac, mir, mar = enhance(img, imgEn, mic, mac, mir, mar)
submitSecure(puzzle, "b", countImg(img))
