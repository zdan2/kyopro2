from sortedcontainers import SortedList
s=SortedList()
q=int(input())
for _ in range(q):
    a=list(map(int,input().split()))
    j=a[0]
    if j==1:
        s.add(a[1])
    if j==2:
        idx=s.bisect_right(a[1])
        if idx<a[2]:
            print(-1)
        else:
            print(s[idx-a[2]])
    if j==3:
        idx=s.bisect_left(a[1])
        if idx+a[2]-1>=len(s):
            print(-1)
        else:
            print(s[idx+a[2]-1])