from collections import Counter
n,k=map(int,input().split())
c=Counter(input().split()).most_common()
a=c[0][1]
print(sum(v>a-2 for _,v in c))