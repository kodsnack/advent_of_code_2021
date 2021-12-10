def solve(lines):
    score = 0
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
                        score += 3
                        break
                elif c == ']':
                    if stack and stack[-1] == '[':
                        stack.pop()
                    else:
                        score += 57
                        break
                elif c == '}':
                    if stack and stack[-1] == '{':
                        stack.pop()
                    else:
                        score += 1197
                        break
                elif c == '>':
                    if stack and stack[-1] == '<':
                        stack.pop()
                    else:
                        score += 25137
                        break
    return score

if __name__ == '__main__':
    lines = []
    with open('10.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines))
