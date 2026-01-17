n,k,x=map(int,input().split())
a=sorted(list(map(int,input().split())))
a=a[:k][::-1]
ox=x
i=0
while x>0 and i<len(a):
    x-=a[i]
    i+=1
if i>k or sum(a)<ox:
    print(-1)
else:
    print(n-k+i)