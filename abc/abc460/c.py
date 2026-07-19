from sortedcontainers import SortedList
input()
a=SortedList(map(int,input().split()))
b=SortedList(map(int,input().split()))
c=0
while a and b:
    if b[0]>a[0]*2:
        a.pop(0)
    else:
        a.pop(0)
        b.pop(0)
        c+=1
print(c)         