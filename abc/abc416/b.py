s=list(input())
f=True
for i in range(len(s)):
    if f and s[i]=='.':
        s[i]='o'
        f=False
    if not f and s[i]=='#':
        f=True
print(''.join(s))