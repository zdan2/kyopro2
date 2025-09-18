n,l,t,x=map(int,input().split())
co=0
time=0
for _ in range(n):
    a,b=map(int,input().split())
    if b>=l and a>t:
        print('forever')
        exit()
    if b>=l:
        co+=a
    else:
        co=0
    if co>=t:
        time+=co-t
        time+=x+a
        if co==t:
            co=0
        else:
            co=a
    else:
        time+=a
print(time)