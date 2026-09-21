from sortedcontainers import SortedList
n=int(input())
s=SortedList(map(int,input().split()))
c=0
while s:
    if len(s)==1:
        break
    a=s.pop(0)
    b=s.pop(0)
    c+=a+b
    s.add(a+b)
print(c)