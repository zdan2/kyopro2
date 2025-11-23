n=int(input())
a=[[*map(int,input().split())] for _ in range(n)]
a=sorted(a,key=lambda x: x[1])
c=1
t=a[0][1]
for i in range(1,n):
    if a[i][0]<=t:
        continue
    t=a[i][1]
    c+=1
print(c)