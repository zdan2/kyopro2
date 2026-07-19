from sortedcontainers import SortedList
x=int(input())
l=SortedList()
l.add(x)
r=SortedList()
q=int(input())
for _ in range(q):
    a,b=map(int,input().split())
    l.add(a)
    l.add(b)
    while len(l)-1>len(r):
        r.add(l.pop())
    while l[-1]>r[0]:
        tl=l.pop()
        tr=r.pop(0)
        l.add(tr)
        r.add(tl)
    print(l[-1])
    