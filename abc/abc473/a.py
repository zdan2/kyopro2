from collections import Counter
input()
print(sum(k for k,v in Counter(map(int,input().split())).items() if v%2!=0))