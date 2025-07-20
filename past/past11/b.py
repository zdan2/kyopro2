from collections import Counter
s=list(input())
r=[s[i]+s[i+1] for i in range(len(s)-1)]
mc=sorted(Counter(r).most_common(),key=lambda x:[-x[1],x[0]])
print(mc[0][0])