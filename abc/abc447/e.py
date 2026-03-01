class UF:
    def __init__(self,n):
        self.parent=list(range(n+1))
        self.size=[1]*(n+1)
        self.history=[]

    def find(self,x):
        if self.parent[x]==x:
            return x
        return self.find(self.parent[x])
    
    def merge(self,x,y):
        x=self.find(x)
        y=self.find(y)
        
        if x==y:
            self.history.append([-1,-1,-1,-1])
            return False
        
        if self.size[x]<self.size[y]:
            x,y=y,x
        
        self.history.append([x,y,self.parent[y],self.size[x]])
        
        self.parent[y]=x
        self.size[x]+=self.size[y]
        return True
    
    def undo(self):
        if not self.history:
            return
        
        x,y,pre_parent_y,pre_size_x=self.history.pop()
        if x==-1:
            return
        self.parent[y]=pre_parent_y
        self.size[x]=pre_size_x

n,m=map(int,input().split())
uf=UF(n)
g=[tuple(map(int,input().split())) for _ in range(m)]
r=[]
for i in range(m-1,-1,-1):
    u,v=g[i]
    uf.merge(u,v)
    root=uf.find(u)

for i in range(m):
    uf
