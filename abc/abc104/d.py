mod=10**9+7
s=list(input())
ca=0
cab=0
cabc=0
for i,e in enumerate(s):
    if e=='?':
        ca*=3
        cab*=3
        cabc*=3
    else:
        ca+=ca
        cab+=cab
        cabc+=cabc
    if e in 'C?':
        cabc+=cab
        cabc%=mod
    if e in 'B?':
        cab+=ca
        cab%=mod
    if e in 'A?':
        ca+=1
    print(e,ca,cab,cabc)

        