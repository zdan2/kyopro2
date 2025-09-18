from bisect import bisect_left
ly=[2002,2020,2022,2200,2202,2222]
ld=[2,22]
sid=['02','22']
y,m,d=map(int,input().split('/'))
if d>22:
    d=2
    m+=1
elif d>2:
    d=22
if m>2:
    y+=1
yid=bisect_left(ly,y)
did=bisect_left(ld,d)
if yid>5:
    print('3000/03/03')
    exit()
print(str(ly[yid])+'/02/'+sid[did])