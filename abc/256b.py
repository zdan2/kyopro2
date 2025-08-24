n=int(input())
a=list(map(int,input().split()))
h=[False]*4
p=0
for e in a:
    h[0]=True
    for i in range(3,-1,-1):
        if h[i] and i+e>3:
            p+=1
            h[i]=False
        elif h[i]:
            h[i+e]=True
            h[i]=False
print(p)