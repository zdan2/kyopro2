n=int(input())
c=[0,0,0]
for e in map(int,input().split()):
    a=1000-e%1000
    for i in range(3):
        c[i]+=a%10
        a//=10
print(*c)