n,c1,c2=input().split()
s=list(input())
for i in range(int(n)):
    if s[i]!=c1:
        s[i]=c2
print(''.join(s))