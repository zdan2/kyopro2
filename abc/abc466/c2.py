n=int(input())
s=[(1,n)]
d=set()
b=[]
c=[]
while s:
    l,r=s.pop()
    print('?',l,r)
    a=input()
    if a=='Yes':
        b.append((l,r))
    else:
        if b:
            b.sort()
            c.append((b[0][0],b[-1][-1]))
            b=[]
        mid=(l+r)//2
        if mid-l>0:
            if (l,mid) not in d:
                s.append((l,mid))
                d.add((l,mid))
        if r-mid>0:
            if (mid,r) not in d:
                s.append((mid,r))
                d.add((mid,r))
if b:
    b.sort()
    c.append((b[0][0],b[-1][-1]))
e=sum((r-l)*(r-l+1)//2 for l,r in c)
print('!',e)