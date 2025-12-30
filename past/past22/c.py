v='aeiou'
r=''
for e in input():
    if e in v:
        r+=e.upper()
    else:
        r+=e
print(r)