n=int(input())
s=list(input())
i=0
t=set()
r=[]
while i<n:
    a=s[i]
    if a in t:
        for j in range(len(r)):
            if r[j]==a:
                r.pop(j)
                break
    r.append(a)
    t.add(a)
    i+=1
print(''.join(r))