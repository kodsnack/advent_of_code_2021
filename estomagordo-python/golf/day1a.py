import sys
p=9**9
n=0
for l in sys.stdin:
 if int(l)>p:n+=1
 p=int(l)
print(n)