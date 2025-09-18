h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]
t=[list(input()) for _ in range(h)]

def arr(mx):
    h=len(mx)
    for i in range(h):
        if '#' not in mx[i]:
            continue
        else:
            break
    for j in range(h-1,-1,-1):
        if '#' not in mx[j]:
            continue
        else:
            break
    return mx[i:j+1]

def chk(s,t):
    sh=len(s)
    sw=len(s[0])
    th=len(t)
    tw=len(t[0])
    
    for i in range(sh-th+1):
        for j in range(sw-tw+1):
            h=1
            for k in range(th):
                for l in range(tw):
                    if s[i+k][j+l]=='#' and t[k][l]=='#':
                        h=0
                        break
                if h==0:
                    break
            if h==1:
                return True
    return False                
    
    
    

tf=arr(t)
rtf=[]
for r in zip(*tf[::-1]):
    rtf.append(r)
tf0=arr(rtf)
tfx=tf0[::-1]
tf1=[]
for r in tfx:
    tf1.append(r[::-1])
tf2=[]
for r in zip(*tf1[::-1]):
    tf2.append(r)
tfx=tf2[::-1]
tf3=[]
for r in tfx:
    tf3.append(r[::-1])
tfs=[tf0,tf1,tf2,tf3]
for t in tfs:
    a=chk(s,t)
    if a:
        print('Yes')
        exit()
print('No')


