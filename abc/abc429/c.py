from collections import Counter
n=int(input())
a=list(map(int,input().split()))
c=Counter(a)
r=0
for v in c.values():
    r+=v*(v-1)//2*(n-v)
print(r)