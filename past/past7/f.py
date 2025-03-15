from collections import defaultdict

d=defaultdict(list)

n=int(input())

for _ in range(n):
    a,l,r=map(int,input().split())
    d[a].append((l,r))

r=[]
for k,v in d.items():
    r.append(sorted(v,key=lambda x:x[1]))

for e in r:
    for i in range(len(e)-1):
        if e[i][1]>e[i+1][0]:
            print('Yes')
            exit()
print('No')
