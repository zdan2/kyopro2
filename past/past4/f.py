from collections import Counter

n,k=map(int,input().split())

r=[]
for _ in range(n):
    r.append(input())

cr=Counter(r)
mcr=cr.most_common()

if k <= 0 or k > len(mcr):
    print('AMBIGUOUS')
else:
    fk = mcr[k-1][1]
    prev = (k > 1) and (fk == mcr[k-2][1])
    next = (k < len(mcr)) and (fk == mcr[k][1])

    if not prev and not next:
        print(mcr[k-1][0])
    else:
        print('AMBIGUOUS')