q=int(input())
h=-1
v=0
for _ in range(q):
    a=int(input())
    if a==1:
        v+=1
    elif a==2:
        v=max(v-1,0)
    else:
        h*=-1
    print('Yes' if v>2 and h==1 else 'No')