
'''
000 0
010 1
011 0
111 1
121 2
221 1
110 0
111 1
211 2
'''
n,q=map(int,input().split())
a=[0]*n
c=0
bit=[]
for _ in range(q):
    s=input().split()
    if s[0]=='1':
        b=int(s[1])-1
        old=a[b]
        c^=old^(old+1)
        if old==0:
            bit.append(b)
        a[b]+=1
    else:
        n_bit=[]
        for x in bit:
            old=a[x]
            c^=old^(old-1)
            a[x]-=1
            if a[x]>0:
                n_bit.append(x)
        bit=n_bit
    print(c)