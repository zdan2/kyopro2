h,w,q=map(int,input().split())
for _ in range(q):
    a,b=map(int,input().split())
    if a==2:
        print(h*b)
        w-=b
    else:
        print(w*b)
        h-=b