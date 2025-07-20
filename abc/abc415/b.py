s=list(input())
r=[]
for i,e in enumerate(s):
    if e=='#':
        r.append(str(i+1))
    if len(r)==2:
        print(r[0]+','+r[1])
        r=[]
print(*r)