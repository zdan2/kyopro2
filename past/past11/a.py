x,a,b,c=map(int,input().split())
t=x/b
r=x/a+c
if t==r:
    print('Tie')
elif t>r:
    print('Hare')
else:
    print('Tortoise')