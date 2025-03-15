from collections import Counter
n=input()
c=Counter(n)
if c['1']==1 and c['2']==2 and c['3']==3:
    print('Yes')
else:
    print('No')