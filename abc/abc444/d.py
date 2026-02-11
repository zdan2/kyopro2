n=int(input())
a=list(map(int,input().split()))
ma=max(a)
d=[0]*ma
for e in a:
    d[e-1]+=1
for i in range(ma-1,0,-1):
    d[i-1]+=d[i]
d+=[0]*(d[-1])
i=0
while i<len(d):
    carry=d[i]//10
    d[i]%=10
    if carry:
        if i+1==len(d):
            d.append(0)
        d[i+1]+=carry
    i+=1
while len(d)>1 and d[-1]==0:
    d.pop()
print(''.join(map(str,d[::-1])))