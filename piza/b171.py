d={'0':{'1':4,'0':0},'1':{'2':5,'1':0},'2':{'0':3,'3':2,'2':0},'3':{'0':3,'4':3,'3':0},'4':{'5':3,'4':0},'5':{'5':0,'6':1,'0':3},
   '6':{'6':0,'7':5},'7':{'7':0,'8':4},'8':{'9':1,'8':0},'9':{'0':2,'9':0}}

hh,mm=input().split(':')
k=int(input())

pre_hour=hh
pre_min=mm

while k>=0:    
    if int(pre_min)+1==60:
        if int(pre_hour)+1==24:
            nxt_hour='00'
            nxt_min='00'
        else:
            nxt_hour=str(int(pre_hour)+1).zfill(2)
            nxt_min='00'
    else:
        nxt_hour=pre_hour
        nxt_min=str(int(pre_min)+1).zfill(2)
        
    k-=d[pre_hour[0]][nxt_hour[0]]
    k-=d[pre_hour[1]][nxt_hour[1]]
    k-=d[pre_min[0]][nxt_min[0]]
    k-=d[pre_min[1]][nxt_min[1]]
    p=pre_hour
    m=pre_min
    pre_hour=nxt_hour
    pre_min=nxt_min
print(p+':'+m)
            
        