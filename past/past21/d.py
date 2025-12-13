from collections import Counter
s=input()
c=Counter(s)
t=''
for e in s:
    if c[e]==1:
        t+=e
print(t)