from collections import Counter
print(int(input())-Counter(input().split()).most_common()[0][1])