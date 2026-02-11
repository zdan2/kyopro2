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
    n1=''
    for e in s1:
        n1+=str(d[e])
    n2=''
    for e in s2:
        n2+=str(d[e])
    n3=''
    for e in s3:
        n3+=str(d[e])
    if n1[0]=='0' or n2[0]=='0' or n3[0]=='0':
        continue
    if int(n1)+int(n2)==int(n3):
        print(n1)
        print(n2)
        print(n3)
        exit()
print('UNSOLVABLE')