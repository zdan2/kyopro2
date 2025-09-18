s=input()
if s[3]!='-':
    print('No')
    exit()
s=s.replace('-','')
if s.isdecimal():
    print('Yes')
else:
    print('No')