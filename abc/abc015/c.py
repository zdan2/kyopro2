n,k=map(int,input().split())
t=[list(map(int,input().split())) for _ in range(n)]
def f(i,x):
    if i==n:
        return x==0
    for j in range(k):
        if f(i+1,x^t[i][j]):
            return True
    return False
res=f(0,0)
print('Found' if res else 'Nothing')