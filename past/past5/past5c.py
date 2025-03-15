n=int(input())
if n==0:
    print(0)
    exit()
r=[]
t='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
t=list(t)
while n>0:
   r.append(n%36)
   n//=36
rr=r[::-1]
a=[]
for e in rr:
    a.append(t[e])
print(''.join(a))