s,t=input().split()
if s[0]=='B':
    s=-(int(s[1]))+1
else:
    s=int(s[0])
if t[0]=='B':
    t=-int(t[1])+1
else:
    t=int(t[0])
print(abs(s-t))