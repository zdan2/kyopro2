n=int(input())
r=[0]*n
p=list(map(int,input().split()))
p=[(e-i)%n for i,e in enumerate(p)]
for e in p:
    r[e]+=1
r+=r
c=0
for i in range(len(r)-2):
    c=max(c,r[i]+r[i+1]+r[i+2])
print(c)