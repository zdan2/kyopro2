n=int(input())
r=[]
for i in range(1,n+1):
    c=input().count('o')
    r.append((i,c))
r=sorted(r,key=lambda x:[-x[1],x[0]])
a=[w for w,_ in r]
print(*a)