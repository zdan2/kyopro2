n=int(input())
pt=0
c=0
for _ in range(n):
    t,v=map(int,input().split())
    c=max(c-(t-pt),0)
    c+=v
    pt=t
print(c)