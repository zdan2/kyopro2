from collections import Counter
a=list(map(int,input().split()))
ca=Counter(a)
c=0
for _,v in ca.items():
    c+=v//2
print(c)
        