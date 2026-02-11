from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
b=[e%200 for e in a]
bi=defaultdict(list)
c=b.pop()
for i,e in enumerate(b):
    bi[e].append(i)
dp=[set() for _ in range(400)]
dp[c].add(n-1)
print(bi)
for k,v in bi.items():
    if dp[k]:
        ba=set(v[0])
        ca=dp[k]
        break
    for j in range(len(v)):
        for i in range(199,-1,-1):
            if dp[i]:
                if dp[i+k]:
                    ba=dp[i]
                    ca=dp[i+k]
                    print(ba)
                    print(ca)
                    exit()
                    break
                else:
                    dp[i+k]=dp[i].copy()
                    dp[i+k].add(v[j])
else:
    for i in range(200):
        print(dp[i],dp[i+200])
    for i in range(200,400):
        if dp[i%200] and dp[i]:
            print(dp[i%200],dp[i])
            break
    else:
        print('No')
    exit()
print(dp)
print(ba,ca)
    


    