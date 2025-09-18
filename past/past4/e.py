from itertools import permutations
n=int(input())
s=input()
for i in permutations(s,n):
    t=''.join(i)
    if t!=s and t[::-1]!=s:
        print(t)
        exit()
print('None')