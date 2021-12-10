def solve(lines):
    scores = []
    for l in lines:
        inp = list(l)
        stack = []
        while inp:
            c = inp.pop(0)
            if c in '{[(<':
                stack.append(c)
            else:
                if c == ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        break
                elif c == ']':
                    if stack and stack[-1] == '[':
                        stack.pop()
                    else:
                        break
                elif c == '}':
                    if stack and stack[-1] == '{':
                        stack.pop()
                    else:
                        break
                elif c == '>':
                    if stack and stack[-1] == '<':
                        stack.pop()
                    else:
                        break
        score = 0
        if not inp:
            while stack:
                c = stack.pop(-1)
                score *= 5
                score += {'(':1,'[':2,'{':3,'<':4}[c]
            scores.append(score)
    return sorted(scores)[int(len(scores)/2)]

if __name__ == '__main__':
    lines = []
    with open('10.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))
