n=int(input())
a=[]
b=0
for _ in range(n):
    s,c=input().split()
    a.append(s)
    b+=int(c)
a.sort()
idx=b%n
print(a[idx])
