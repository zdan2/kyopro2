from collections import defaultdict
d={}

test=['tree','treeth','time','paiza','path']

for e in test:
    cr=d
    for l in e:
        if l not in cr:
            cr[l]={}
        cr=cr[l]
    cr['#']={}

print(d)
         
        
        