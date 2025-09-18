s=input()
c=0
if s[0]=='o':
    c+=1
if s[-1]=='i':
    c+=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
print(c)