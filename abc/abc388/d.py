n=int(input())
a=list(map(int,input().split()))
ageru=n-1
morau=0
motteru=0
for i in range(n):
    a[i]+=min(morau,motteru)#ageta
    motteru-=min(morau,motteru)#motterumonokarahiita
    motteru+=+min(ageru,a[i])
    a[i]-=min(a[i],ageru)
    ageru-=1
    morau+=1
print(a)