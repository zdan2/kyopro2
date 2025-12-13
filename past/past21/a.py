x=int(input())
h=11 if x>0 else 12
m=60-x if x>0 else -x
print(str(h)+':'+str(m).zfill(2))