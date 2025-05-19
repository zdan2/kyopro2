from collections import deque
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
q=deque()
for i in range(n):
    if a[i]!=b[i]:
        q.append((i,a[i],b[i]))
c=0
while q:
    pi,pa,pb=q.popleft()
    ni,na,nb=q.popleft()
    if pi+1==ni and pa==nb and pb==na:
        c+=1
    elif pi+1==ni and pa==nb and pb!=na:
        c+=1
        q.appendleft((ni,na,pb))
    elif pi+1==ni and pb==na and pa!=nb:
        c+=1
        q.appendleft((ni,pa,nb))
    else:
        print('No')
        exit()
    if c==2:
        break
if len(q)==0 and c==2:
    print('Yes')
else:
    print('No')