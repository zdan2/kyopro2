from itertools import permutations
s1=list(input())
s2=list(input())
s3=list(input())
s=set(s1+s2+s3)
ss=sorted(s)
nums=[0,1,2,3,4,5,6,7,8,9]
p=list(permutations(nums,len(s)))
for e in p:
    d={}
    for i,l in enumerate(ss):
        d[l]=e[i]
    n1=0
    b=10*(len(s1)-1)
    for i,e in enumerate(s1):
        n1+=10**(b-i)*d[e]
    if n1<b:
        continue
    n2=0
    b=10*(len(s2)-1)
    for i,e in enumerate(s2):
        n2+=10**(b-i)*d[e]
    if n2<b:
        continue
    n3=0
    b=10*(len(s3)-1)
    for i,e in enumerate(s3):
        n3+=10**(b-i)*d[e]
    if n3<b:
        continue
    if n1+n2==n3:
        print(n1)
        print(n2)
        print(n3)
        exit()
print('UNSOLVABLE')