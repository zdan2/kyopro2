n=int(input())
r=[]
for _ in range(n):
    s=input()
    for i in range(len(s)):
        if s[i]!='0':
            r.append((len(s[i:]),s,s[:i]))
            break
r=sorted(r,key=lambda x:[x[0],x[1],x[2]])
for e in r:
    print(e[1])