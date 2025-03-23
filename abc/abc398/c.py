from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
s=defaultdict(int)
can=[]
for i in range(n):
    if s[a[i]]==0:
        can.append((a[i],i+1))
    s[a[i]]+=1
r=0
mi=-1
for num,i in can:
    if s[num]==1:
        if a[i-1]>r:
            r=a[i-1]
            mi=i
print(mi)