h,w=map(int,input().split())
y,x=map(int,input().split())
y-=1
x-=1
mx=[list(input()) for _ in range(h)]
while True:
    if 0<=x-1 and mx[y][x-1]=='.':
        while True:
            x-=1
            if x==0 or mx[y][x-1]=='#':
                break
        y+=1
    elif x+1<w and mx[y][x+1]=='.':
        while True:
            x+=1
            if x==w-1 or mx[y][x+1]=='#':
                break
        y+=1
    else:
        y+=1
    if y==h-1:
        break
print(y+1,x+1)