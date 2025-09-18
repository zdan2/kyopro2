q=int(input())
s=[]
r=[]
for _ in range(q):
    t=input()
    if t=='READ':
        r.append(s.pop())
    else:
        s.append(t)
for b in r:
    print(b)