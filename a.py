from typing import List
def candy(ratings: List[int]):
        d=[1]
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                d.append(d[-1]+1)
            elif ratings[i]<ratings[i-1]:
                d.append(1)
            else:
                d.append(1)
        f=[1]
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                f.append(f[-1]+1)
            elif ratings[i]<ratings[i+1]:
                f.append(1)
            else:
                f.append(1)
        f=f[::-1]
        md=min(d)
        g=[max(a,b) for a,b in zip(d,f)]
        return sum(g)

c=candy([1,3,4,5,2])
print(c)