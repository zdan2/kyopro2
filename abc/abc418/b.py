s=input()
c=0
for i in range(len(s)):
    for j in range(i,len(s)):
        if j-i<3:
            continue
        if s[i]==s[j]=='t':
            t=s[i:j+1]
            ct=t.count('t')-2
            c=max(c,ct/(j-i-1))
print(c)