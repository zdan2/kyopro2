from collections import Counter
s=list(input())
t=len(s)
for i in range(1,t//2):
    if s[2*i-2]!=s[2*i-1]:
        print('No')
        exit()
cs=Counter(s)
for v in cs.values():
    if v!=2:
        print('No')
        exit()
print('Yes')