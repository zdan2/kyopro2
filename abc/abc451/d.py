from sortedcontainers import SortedSet
n=int(input())
s=SortedSet([2**i for i in range(30)])
l=[str(e) for e in s]
for i in range(n-1):
    a=s.pop(0)
    str_a=str(a)
    for e in l:
        if len(str_a)+len(e)>9:
            continue
        s.add(int(str_a+e))
print(s[0])