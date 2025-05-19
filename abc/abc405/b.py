from collections import Counter,defaultdict
n,m=map(int,input().split())
a=list(map(int,input().split()))
c=Counter(a)
for i in range(1,max(a)+1):
    if i not in c:
        print(0)
        exit()
i=1
while a:
    b=a.pop()
    c[b]-=1
    if c[b]==0:
        print(i)
        exit()
    i+=1