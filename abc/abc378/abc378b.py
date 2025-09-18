n=int(input())
a=[(0,0)]+[tuple(map(int,input().split())) for _ in range(n)]
q=int(input())
for _ in range(q):
    t,d=map(int,input().split())
    w,r=a[t]
    if d%w>r:
        c=(d+w)//w*w+r
    else:
        c=d//w*w+r
    print(c)