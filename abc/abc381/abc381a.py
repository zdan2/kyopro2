n=int(input())
s=list(input())
if s==['/']:
    print('Yes')
    exit()
if n%2==0:
    print('No')
    exit()
if set(s[:(n+1)//2-1])=={'1'} and s[(n+1)//2-1]=='/' and set(s[(n+1)//2:])=={'2'}:
    print('Yes')
else:
    print('No')