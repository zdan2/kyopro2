n=int(input())
s=[list(input()) for _ in range(n)]
dr=[[] for _ in range(2*n-1)]
for i in range(n-1,-1,-1):
    for j in range(n):
        dr[i+j].append(s[i][j])
mx=[]
for r in dr:
    if len(set(r))==1:
        if '?' not in set(r):
            mx.append(r)
            continue
        r=['0']*len(r)
        mx.append(r)
        continue   
    if len(set(r))==2 and '?' in set(r):
        chr=(set(r)^set('?'))
        r=[*chr]*len(r)
        mx.append(r)
    else:
        print(-1)
        exit()
rx=[[0]*n for _ in range(n)]
iters=[iter(d) for d in mx]
for i in range(n-1,-1,-1):
    for j in range(n):
        rx[i][j]=next(iters[i+j])
for r in rx:
    print(''.join(r))