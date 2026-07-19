h,w=map(int,input().split())
t=[list(input()) for _ in range(h)]
j=0
ot=t.copy()
while True:
    if t[0].count('#')==0:
        t.pop(0)
    if t[-1].count('#')==0:
        t.pop()
    t=[list(r) for r in zip(*t)]
    j+=1
    if j==4 and ot==t:
        break
    elif j==4:
        j=0
        ot=t.copy()
for r in t:
    print(''.join(r))