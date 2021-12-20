import sys
p=9**9
n=0
for l in map(int,sys.stdin):
 if l>p:n+=1
 p=l
print(n)