from collections import deque

n=int(input())
s=set()
takahasi=0
aoki=0
ta=[]
ao=[]
for i in range(1,n+1):
    a,b=map(int,input().split())
    ta.append((a,a-b,i))
    ao.append((b,b-a,i))
sta=sorted(ta,key=lambda x:[-x[0],x[1]])
sao=sorted(ao,key=lambda x:[-x[0],x[1]])
sta=deque(sta)
sao=deque(sao)

for _ in range(n):
    while sta:
        x,_,idx=sta.popleft()
        if idx not in s:
            takahasi+=x
            s.add(idx)
            break
    while sao:
        x,_,idx=sao.popleft()
        if idx not in s:
            aoki+=x
            s.add(idx)
            break

print(takahasi-aoki)