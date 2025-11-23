n,m,k=map(int,input().split())
if n<k//2 or m<k//2 or n+m<k:
    print(-1)
    exit()
r=sorted(list(map(int,input().split())),reverse=True)
p=sorted(list(map(int,input().split())),reverse=True)
print(max(sum(r[:k//2])+sum(p[:(k+1)//2]),sum(r[:(k+1)//2])+sum(p[:k//2])))