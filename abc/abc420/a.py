x,y=map(int,input().split())
r=(x+y)%12
print(12 if r==0 else r)