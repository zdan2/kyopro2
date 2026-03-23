s=input()
l=len(s)
v=set()
a=[]
for i in range(l):
    if s[i] not in v:
        v.add(s[i])
    else:
        v.remove(s[i])
    a.append(tuple(sorted(v)))
d={}
c=0
for v in a:
    if not v:
        c+=1
    if v in d:
        c+=d[v]
        d[v]+=1
    else:
        d[v]=1
print(c)