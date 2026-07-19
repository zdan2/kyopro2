n=int(input())
m=[list(map(int,input().split())) for _ in range(n)]
m=sorted(m,key=lambda x:[x[0],-x[1]])
c=0
h=float('inf')
for x,y in m:
    if y<=h:
        c+=1
        h=y
print(c)