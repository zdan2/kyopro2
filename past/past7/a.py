s=list(input())
c=0
for i in range(0,14,2):
   c+=int(s[i])
c*=3
for i in range(1,14,2):
    c+=int(s[i])
if c%10==int(s[-1]) :
    print('Yes')
else:
    print('No')