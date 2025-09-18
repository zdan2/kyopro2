n=int(input())
s=list(input())
v={'a','i','u','e','o'}
for i in range(1,n-1):
    if s[i]=='x' and s[i-1]==s[i+1] and s[i-1] in v:
        s[i+1]='.'
        s[i]='.'
        s[i-1]='.'
print(''.join(s))