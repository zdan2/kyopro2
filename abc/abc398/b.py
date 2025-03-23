from collections import Counter
c=Counter(map(int,input().split())).most_common()
print('Yes' if len(c)>1 and c[0][1]>2 and c[1][1]>1 else 'No')