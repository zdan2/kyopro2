d={}
n=int(input())
a=[]
for _ in range(n):
    m,h=input().split()
    h=int(h)
    d[h]=m
    a.append(h)
a.sort()
print(d[a[-2]])