def er(n):
    n/=4
    sqrt=int(n**0.25)+1
    e=[True]*sqrt
    e[0]=False
    e[1]=False
    for i in range(2,sqrt):
        if e[i]:
            for j in range(i+i,sqrt,i):
                e[j]=False
    d=[i*i for i in range(sqrt) if e[i]]
    return d
a=er(1000000000000)
l=len(a)
r=[]
for i in range(l-1):
    for j in range(i+1,l):
        r.append(a[i]*a[j])
q=int(input())
for _ in range(q):
    n=int(input())
    for el in r:
        

        
    