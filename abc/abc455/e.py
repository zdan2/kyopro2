from collections import defaultdict
n=int(input())
s=input()
ca=0
cb=0
cc=0
r=[]
d=defaultdict(int)
a=[]
for i in range(n):
    if s[i]=='A':
        ca+=1
    elif s[i]=='B':
        cb+=1
    else:
        cc+=1
    r.append((ca,cb,cc))
for i,(ca,cb,cc) in enumerate(r):
    d[(ca-cb,'*','*')]+=1
    d[('*',cb-cc,'*')]+=1
    d[('*','*',cc-ca)]+=1
    d[(ca-cb,cb-cc,'*')]+=1
    d[(ca-cb,'*',cc-ca)]+=1
    d[('*',cb-cc,cc-ca)]+=1
    d[(ca-ca,cb-cc,cc-ca)]+=1
    
