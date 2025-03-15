n,m=map(int,input().split())
lr=[tuple(map(int,input().split())) for _ in range(n)]
slr=sorted(lr,key=lambda x:x[1])
c=0
ll=[1]
for l,r in slr:
  x=ll[-1]
  for i in range(x,r):
    c+=r-i
    if i==l:
      break
  if l>=ll[-1]:
    ll.append(l+1)
  else:
    ll.append(ll[-1]+1)  

print(c+1 if c>0 else 0)