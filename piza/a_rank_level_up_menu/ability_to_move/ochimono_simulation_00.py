h,w,n=map(int,input().split())
height=[0]*w
mx=[['.']*w for _ in range(h)]
for _ in range(n):
    y,x,p=map(int,input().split())
    row=max(height[p:p+x])
    for k in range(p,p+x):
        for l in range(row,row+y):
            mx[l][k]='#'
            height[k]=l+1
for r in mx[::-1]:
    print(''.join(r))