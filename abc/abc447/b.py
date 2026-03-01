from collections import Counter
s=input()
c=Counter(s).most_common()
m=c[0][1]
for k,v in c:
    if v<m:
        break
    s=s.replace(k,'')
print(s)