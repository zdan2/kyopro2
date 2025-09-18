n=int(input())
start=600
r=[]
f=1
nxt_start=start
for _ in range(n):
    name,time=input().split()
    time=int(time)
    nxt_end=nxt_start+time
    if nxt_end>721 and f==1:
        nxt_start+=50
        nxt_end+=50
        f=0
    r.append((nxt_start,nxt_end,name))
    nxt_start=nxt_end+10
for e in r:
    print(f'{e[0]//60}:{e[0]%60:02} - {e[1]//60}:{e[1]%60:02} {e[2]}')