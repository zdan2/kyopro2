x,y=map(int,input().split())
a,b,c=0,0,0
for i in range(1,7):
    for j in range(1,7):
        if i+j>=x:
            a+=1
        if abs(i-j)>=y:
            b+=1
        if i+j>=x and abs(i-j)>=y:
            c+=1
print((a+b-c)/36)