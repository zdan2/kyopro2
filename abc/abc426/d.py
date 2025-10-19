t=int(input())
for _ in range(t):
    n=int(input())
    m1=0
    m0=0
    c1=1
    c0=1
    a0=0
    a1=0
    s=list(input())+['#']
    for i in range(n):
        if s[i]=='0':
            a0+=1
        else:
            a1+=1
        if s[i]==s[i+1]=='0':
            c0+=1
        else:
            m0=max(m0,c0)
            c0=1
        if s[i]==s[i+1]=='1':
            c1+=1
        else:
            m1=max(m1,c1)
            c1=1
    r0=(a0-m0)*2+a1
    r1=(a1-m1)*2+a0
    print(min(r0,r1))
    