from collections import Counter
n,k=map(int,input().split())
s=input()
r=sorted(Counter([s[i:i+k] for i in range(n-k+1)]).most_common(),key=lambda x: [-x[1],x[0]])
c=r[0][1]
a=[e[0] for e in r if e[1]==c]
print(c)
print(*a)