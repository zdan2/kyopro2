def f(s):
    l=len(s)
    can=''
    r=[s[0]]
    for i in range(1,l):
        if s[i]=='x' and r[-1]=='x':
            r.pop()
            r.append('c')
        elif len(r)>1 and s[i]==')' and r[-2]=='(' and r[-1]=='c':
            r.pop()
            r.pop()
            if r and r[-1]=='x':
                r.pop()
                r.append('c')
                r.append('x')
            else:
                r.append('c')
        else:
            r.append(s[i])
    return r

n=int(input())
for _ in range(n):
    a=input()
    b=input()
    print('Yes' if f(a)==f(b) else 'No')