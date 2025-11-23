s=input()
x='X'
l=s.index(x)
r=s.rindex(x)
print(s[:l]+s[l+1:r][::-1]+s[r+1:])