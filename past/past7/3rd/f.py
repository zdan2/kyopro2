n=int(input())
r=[]
for _ in range(n):
    d,s,t=map(int,input().split())
    r.append((d*24+s,d*24+t))
r=sorted(r,key=lambda x:[x[1],x[0]])
pe=0
for s,e in r:
    if pe<=s:
        pe=e
        continue
    print('Yes')
    exit()
print('No')