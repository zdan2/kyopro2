from collections import defaultdict
h,w,d=map(int,input().split())

mx=[list(input()) for _ in range(h)]
v=defaultdict(set)
for i in range(h):
    for j in range(w):
        if mx[i][j]=='.':
            c=0 
            for k in range(h):
                for l in range(w):
                    if abs(i-k)+abs(j-l)<=d and mx[k][l]=='.':
                        v[(i,j)].add((k,l))
c=0        
for k1,s1 in v.items():
    for k2,s2 in v.items():
        if k1!=k2:
            c=max(c,len(s1|s2))
print(c)