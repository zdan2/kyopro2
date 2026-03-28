n,m=map(int,input().split())
s=[0]*m
for _ in range(n):
    a,b=map(int,input().split())
    s[a-1]-=1
    s[b-1]+=1
for e in s:
    print(e)