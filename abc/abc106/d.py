k,m,q=map(int,input().split())
n=[[0,0] for _ in range(k+2)]
for _ in range(m):
    l,r=map(int,input().split())
    n[l][0]+=1
    n[r+1][1]+=1
print(n)
for i in range(1,k+2):
    n[i][0]+=n[i-1][0]
    n[i][1]+=n[i-1][1]
print(n)
for _ in range(q):
    p,q=map(int,input().split())
    print(n[q+1][1]-n[p][1])
    
