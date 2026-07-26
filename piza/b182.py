h,w,n=map(int,input().split())
y,x=map(int,input().split())
y-=1
x-=1
m=[list(input()) for _ in range(h)]
r=n//2
left=max(0,x-r)
right=min(w-1,x+r)
up=max(0,y-r)
btm=min(y+r,h-1)
c=0
for i in range(up,btm+1):
    for j in range(left,right+1):
        if m[i][j]=='.':
            c+=1
print(c)