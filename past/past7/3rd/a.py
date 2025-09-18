s=input()
a=0
b=0
for i in range(0,14,2):
    a+=int(s[i])
    b+=int(s[i+1])
r=(a*3+b)%10
if r==int(s[14]):
    print('Yes')
else:
    print('No')