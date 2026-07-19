from collections import defaultdict
k=int(input())
sqrt=int(k**0.5)+1
d=defaultdict(int)
for i in range(2,sqrt):
    if k%i==0:
        while k%i==0:
            d[i]+=1
            k//=i
d[k]+=1
r=sorted([k+v-1 for k,v in d.items()])
print(r[-1])
