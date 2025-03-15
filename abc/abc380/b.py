s=list(input())
c=0
r=[]
for i in range(1,len(s)):
    if s[i]=='|':
        r.append(c)
        c=0
    else:
        c+=1
print(*r)
    
        