from collections import deque
s=input()
t=input()
c=[-1]*len(t)
a=0
for i,e in enumerate(s):
    for j in range(len(t)-1,-1,-1):
        if e==t[j]:
            if j==0:
                c[0]=i
            elif c[j-1]!= -1:
                c[j]=c[j-1]
    if c[-1]!=-1:
        a+=c[-1]+1
print(len(s)*(len(s)+1)//2-a)