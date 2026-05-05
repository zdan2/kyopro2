from collections import Counter
n,k=map(int,input().split())
print(sum(sorted([k*v for k,v in Counter(map(int,input().split())).items()])[:-k]))