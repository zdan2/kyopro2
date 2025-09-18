k=int(input())
cards=[k]*9
point1=[0]*9
point2=[0]*9
s=list(input())
t=list(input())
for i in range(4):
    p1=int(s[i])-1
    cards[p1]-=1
    point1[p1]+=1
    p2=int(t[i])-1
    cards[p2]-=1
    point2[p2]+=1
r=0
for i in range(9):
    if cards[i]>0:
        fc=cards[i]/(k*9-8)
        cards[i]-=1
        point1[i]+=1
        score1=0
        for ii,e in enumerate(point1):
            score1+=(ii+1)*(10**e)
        for j in range(9):
            if cards[j]>0:
                point2[j]+=1
                score2=0
                for jj,ee in enumerate(point2):
                    score2+=(jj+1)*(10**ee)
                if score1>score2:
                    r+=fc*cards[j]/(k*9-9)
                point2[j]-=1
        point1[i]-=1
        cards[i]+=1
print(r)