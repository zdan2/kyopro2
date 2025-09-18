n,l=map(int,input().split())
if l%3!=0:
    print(0)
    exit()
d=list(map(int,input().split()))
p=[0]*l
p[0]=1
c=0
for e in d:
    p[(c+e)%l]+=1
    c=(c+e)%l
s=l//3
c=0
for i in range(s):
   c+=p[i]*p[i+s]*p[i+2*s]
print(c) 