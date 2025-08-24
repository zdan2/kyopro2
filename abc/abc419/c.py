n=int(input())
x_min=float('inf')
x_max=0
y_min=float('inf')
y_max=0
for _ in range(n):
    x,y=map(int,input().split())
    x_min=min(x_min,x)
    x_max=max(x_max,x)
    y_min=min(y_min,y)
    y_max=max(y_max,y)
print((max(x_max-x_min,y_max-y_min)+1)//2)