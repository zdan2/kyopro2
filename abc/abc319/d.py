from bisect import bisect
n,m=map(int,input().split())
l=list(map(int,input().split()))
cl=[l[0]+1]
for i in range(1,n):
    cl.append(cl[-1]+l[i]+1)
cl.append(float('inf'))
if m==1:
    print(cl[-2]-1)
    exit()
left=max(l)
right=cl[-2]
mid=(left+right)//2
a=float('inf')
while left<=right:
    p=0
    pre=0
    r=[]
    while p<m:
        idx=bisect(cl,(mid+1)+pre+p)-1
        p+=1
        pre=cl[idx]-1
        r.append((idx,cl[idx]-1))
    if idx<n-1:
        left=mid+1
    else:
        a=min(a,mid)
        right=mid-1
    mid=(left+right)//2
print(a)    