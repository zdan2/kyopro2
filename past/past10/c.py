a=input()
la=len(a)
ra=(3 if la%3==0 else la%3)
ca=(la-1)//3
print(a[:ra]+(chr(ord('a')+ca-1)))