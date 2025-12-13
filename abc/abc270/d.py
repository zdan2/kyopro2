import heapq

n,k=map(int,input().split())
a=list(map(int,input().split()))
hq=[-e for e in a]
heapq.heapify(hq)

turn=0
score=0

remain=n

while remain>0:
    can = heapq.heappop(hq)
    can*=-1
    if can>remain:
        continue
    gets=remain//can
    if turn==0:
        score+=can*((gets+1)//2)
    else:
        score+=can*(gets//2)
    turn=(turn+gets)%2
    remain-=can*gets

print(score)