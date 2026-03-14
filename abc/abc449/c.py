from bisect import bisect_left,bisect_right
from collections import defaultdict
d=defaultdict(list)
n,l,r=map(int,input().split())
s=input()
c=0
for i in range(n):
    if d[s[i]]:
        a=d[s[i]]
        li=bisect_left(a,i-r)
        ri=bisect_right(a,i-l)
        c+=ri-li
    d[s[i]].append(i)
print(c)