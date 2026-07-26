m,d=map(int,input().split())
s=['*']+list(input())+['*']
for i in range(m+1):
    if s[i]=='G':
        for j in range(d+1):
            if s[i+j]=='*':
                break
            if s[i+j]=='.':
                s[i+j]='#'
for i in range(m,0,-1):
    if s[i]=='G':
        for j in range(d+1):
            if s[i-j]=='*':
                break
            if s[i-j]=='.':
                s[i-j]='#'
print(s.count('.'))