n=int(input())
s=[]
c=[]
d={'(':0,')':0}
for _ in range(n):
    a=list(input().split())
    if a[0]=='1':
        d[a[1]]+=1
        if d['(']<d[')']:
            c.append(len(s))
        s.append(a[1])
    else:
        b=s.pop()
        d[b]-=1
        if c and len(s)==c[-1]:
            c.pop()
    if len(c)==0 and d['(']==d[')']:
        print('Yes')
    else:print('No')