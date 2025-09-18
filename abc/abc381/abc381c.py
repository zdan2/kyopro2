n=int(input())
s=list(input())

co=0
r=0
h=0

for i in range(n):
    if s[i]=='/':
        h=1
    
    if s[i]=='1':
        co+=1
    elif co>0 and s[i]=='/':
        ct=0
        j=i+1
        while j<n and s[j]=='2':
            ct+=1
            j+=1
        r=max(r,min(co,ct)*2+1)
        co=0
        ct=0
    else:
        co=0
        
if r==0 and h==1:
    print(1)
else:
    print(r)    