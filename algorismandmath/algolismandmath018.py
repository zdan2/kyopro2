from collections import Counter
n=int(input())
a=list(map(int,input().split()))
ca=Counter(a)
r=ca[100]*ca[400]+ca[200]*ca[300]
print(r)