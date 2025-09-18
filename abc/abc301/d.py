s=list(input())
n=int(input())
qidx=[]
for i in range(len(s)):
    if s[i]=='?':
        qidx.append(i)
for i,b in enumerate(qidx):
    s[b]='1'
    for j in qidx[i+1:]:
        s[j]='0'
    if int(''.join(s),2)>n:
        s[b]='0'
r=int(''.join(s),2)
if r>n:
    print(-1)
else:
    print(r)