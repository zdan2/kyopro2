s=input()
g=0
c=0
for e in s:
    if e=='p' and g>0:
        g-=1
    elif e=='p' and g==0:
        g+=1
        c-=1
    elif e=='g' and g==0:
        g+=1
    else:
        g-=1
        c+=1
print(c)