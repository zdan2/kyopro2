n=int(input())
a=list(map(int,input().split()))
r=[]
for i in range(n):
    c=0
    j=i
    while True:
        if a[j]-1==i:
            c+=1
            break
        j=a[j]-1
        c+=1
    r.append(c)
print(*r)