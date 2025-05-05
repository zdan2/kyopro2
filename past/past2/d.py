s={'','.'}
t=list(input())
for e in t:
    s.add(e)
r=set()
for l1 in s:
    for l2 in s:
        for l3 in s:
            k=l1+l2+l3
            if len(t)>=len(k):
                r.add(k)
c=set()
for e in r:
    h=0
    for i in range(len(t)-len(e)+1):
        for j in range(len(e)):
            if e[j]=='.':
                continue
            if e[j]!=t[i+j]:
                break
        else:
            h=1
            break
    if h:
        c.add(e)
print(len(c)-1)