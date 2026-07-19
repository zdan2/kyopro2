from random import randint,sample
s=sample(range(1,53),52)
mark={0:'C',1:'D',2:'S',3:'H'}
nums={1:'A',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'J',12:'Q',13:'K'}
card=[mark[e%4]+nums[(e+3)//4] for e in s]
pict={'K','Q','J'}
p1=card[0][1]
p2=card[1][1]
s1,s2=0,0
if p1 in pict:
    s1=10
elif p1 =='A':
    s1=11
else:
    s1=int(p1)
if p2 in pict:
    s2=10
elif p2 =='A':
    s2=11
else:
    s2=int(p2)
score=s1+s2
if score>22 and (p1 or p2) == 'A':
    score-=10
print(card[0],card[1],score)
    

