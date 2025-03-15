n=int(input())
r=[]
while n>1:
   r.append(str(n%2))
   n//=2
r.append("1")
r+=["0"]*(10-len(r))
print("".join(r[::-1])) 