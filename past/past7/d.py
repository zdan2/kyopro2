d={'a' , 'i' , 'u' , 'e' , 'o'}
n=int(input())
s=list(input())
for i in range(n-2):
    if s[i] in d and s[i+1]=='x' and s[i+2]==s[i]:
        s[i],s[i+1],s[i+2]='.','.','.'
print(''.join(s))

