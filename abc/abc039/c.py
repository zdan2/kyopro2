k='WBWBWWBWBWBW'
s='DoReMiFaSoLaSi'
d={}
for i in range(7):
    d[s[i*2:i*2+2]]=k
    k=k[1:]+k[0]
    while k[0]!='W':
        k=k[1:]+k[0]
t=input()
for k,v in d.items():
    if t[:12]==v:
        print(k)
        break