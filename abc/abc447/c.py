s=input()+'*'
t=input()+'*'
def f(s):
    ss=''
    k=[0]
    for i in range(len(s)):
        if s[i]=='A':
            continue
        ss+=s[i]
        k.append(i)
    return ss,k
a,b=f(s)
c,d=f(t)
if a!=c:
    print(-1)
    exit()
print(sum(abs((b[i]-b[i-1])-(d[i]-d[i-1])) for i in range(1,len(a)+1)))