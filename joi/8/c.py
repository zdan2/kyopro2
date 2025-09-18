n=int(input())
c=1
pc=int(input())
r=[]
for _ in range(n-1):
    b=int(input())
    if b==pc:
        c+=1
    else:
        r.append((pc,c))
        c=1
        pc=b
r.append((pc,c))
can=[]
if r[0][1]==1 and r[1][1]==3:
    can.append(0)
for i in range(1,len(r)-1):
    if r[i][1]!=1:
        continue
    if r[i-1][0]==r[i+1][0] and r[i-1][1]+r[i+1][1]>3:
        can.append(i)
if r[-1][1]==1 and r[-2][1]==3:
    can.append(len(r)-1)
if not can:
    print(n)
    exit()
mc=float('inf')
for e in can:
    cr=r[:]
    if e==0:
        cr.pop(1)
        cr.pop(0) 
    elif e==len(r)-1:
        cr.pop(-1)
        cr.pop(-1)
    else:
        cr.pop(e+1)
        cr.pop(e)
        cr.pop(e-1)
    while True:
        h=0
        for i in range(len(cr)-1):
            if cr[i][0]==cr[i+1][0]:
                if cr[i][1]+cr[i+1][1]>=4:
                    h=1
                    break
                else:
                    h=2
                    break
        if h==1:
            cr.pop(i+1)
            cr.pop(i)
        elif h==2:
            _,num=cr.pop(i+1)
            cr[i]=(cr[i][0],cr[i][1]+num)
        else:
            cc=sum(e[1] for e in cr)
            break 
        if len(cr)<3:
            cc=sum(e[1] for e in cr)
            break
    mc=min(mc,cc)
print(mc)