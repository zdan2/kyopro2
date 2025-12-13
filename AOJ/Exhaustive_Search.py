n=int(input())
s=set()
a=list(map(int,input().split()))
def dfs(i,c=0):
    if i==n:
        s.add(c)
        return
    dfs(i+1,c)
    dfs(i+1,c+a[i])
dfs(0)
m=int(input())
for e in list(map(int,input().split())):
    print('yes' if e in s else 'no')