n,m=map(int,input().split())
c=0
while m:
    m=n%m
    c+=1
print(c)