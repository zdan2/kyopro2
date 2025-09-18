n=int(input())
s=[]
a=[]
for _ in range(n):
    c,d=input().split()
    d=int(d)
    s.append(c)
    a.append(d)
idx=a.index(min(a))
for e in (s[idx:n]+s[:idx]):
    print(e)