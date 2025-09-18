from collections import Counter
s=input()
r=[s[i]+s[i+1] for i in range(len(s)-1)]
print(sorted(Counter(r).most_common(), key=lambda x:[-x[1],x[0]])[0][0])