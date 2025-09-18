from collections import defaultdict
d=defaultdict(set)
n=int(input())
for _ in range(n):
    c=0
    m=int(input())
    a=list(map(int,input().split()))
    a=[-1]+a+[-2]
    for i in range(1,m):
        if a[i-1]!=a[i] and a[i]!=a[i+1]:
            for e in d[a[i]]:
                print('f',a[i],e)
                if a[i] in d[e]:
                    c+=1
                    break
            else:
                d[a[i]].add(a[i-1])
                d[a[i]].add(a[i+1])
                d(a[i-1]).add(a[i])
                d(a[i+1]).add(a[i])
    print(d)
    print('a',c)
                
    