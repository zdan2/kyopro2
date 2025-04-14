n=int(input())
emp=[[],[]]
sar=[None]*(n+1)
for i in range(n-1):
    a=int(input())
    emp.append([])
    emp[a].append(i+2)
for i in range(n,0,-1):
    if not emp[i]:
        sar[i]=1
    else:
        can=[]
        for e in emp[i]:
            can.append(sar[e])
        sar[i]=max(can)+min(can)+1
print(sar[1])