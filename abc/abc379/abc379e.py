n=int(input())
s=input()
c=0
r=[]
for i in range(1,n+1):
   c+=int(s[i-1])*i
   r.append(c*10**(n-i))
print(r) 