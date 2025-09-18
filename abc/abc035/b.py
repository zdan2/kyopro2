s=input()
qc=s.count('?')
lc=s.count('L')
rc=s.count('R')
uc=s.count('U')
dc=s.count('D')
x=rc-lc
y=uc-dc
m=[(x+qc,y),(x-qc,y),(x,y+qc),(x,y-qc)]
r=[]
for x,y in m:
    d=abs(x)+abs(y)
    r.append(d)
q=int(input())
if q==1:
    print(max(r))
else:
    print(min(r))