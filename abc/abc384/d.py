n, s = map(int, input().split())
a = list(map(int, input().split()))
r = sum(a)
v = []
for i in range(n):
    # jは終了インデックスとして利用するので、i+1からn+1に
    for j in range(i+1, n+1):
        # a[i:j] はa[i]からa[j-1]まで
        v.append(r - sum(a[i:j]))

if s % r in v:
   print('Yes')
else:
   print('No')


