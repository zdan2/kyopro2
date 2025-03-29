from collections import defaultdict
t=int(input())
for _ in range(t):
    n=int(input())
    d=defaultdict(set)
    s=[0]+list(map(int,input().split()))+[-1]
    c=0
    v=set()
    for i in range(1,n*2):
        if s[i-1]==s[i] or s[i+1]==s[i]:
            continue
        if s[i] not in d:
            d[s[i]].add(s[i-1])
            d[s[i]].add(s[i+1])
        else:
            d[s[i]]&={s[i-1],s[i+1]}
            if d[s[i]]:
                if i not in v:
                    c+=1
                v.add(i)
    print(c)