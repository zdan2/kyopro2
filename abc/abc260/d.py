from sortedcontainers import SortedList
n,k=map(int,input().split())
p=list(map(int,input().split()))
eat=[-1]*n
s=SortedList()
for i,e in enumerate(p):
    if not s:
        if k==1:
            eat[e-1]=i+1
        else:
            s.add(SortedList([e]))
    else:
        idx=s.bisect([e])
        if idx==len(s):
            s.add(SortedList([e]))
        else:
            if len(s[idx])+1==k:
                eat[e-1]=i+1
                for f in s[idx]:
                    eat[f-1]=i+1
                s.pop(idx)
            else:
                s[idx].add(e)
for i in eat:
    print(i)