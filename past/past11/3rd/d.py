class U:
    
    def __init__(self):
        self.parent={chr(i):chr(i) for i in range(ord('a'),ord('z')+1)}
        self.size={chr(i): 1 for i in range(ord('a'), ord('z') + 1)}
    
    def merge(self,a,b):
        root_a=self.find(a)
        root_b=self.find(b)
        if root_a==root_b:
            return
        if self.size[root_a]<self.size[root_b]:
            root_a,root_b,=root_b,root_a
        
        self.parent[root_b]=root_a
        self.size[root_a]+=self.size[root_b]
    
    def find(self,a):
        if self.parent[a]==a:
            return a
        root=self.find(self.parent[a])
        self.parent[a]=root
        return root
    
u=U()
    
n=int(input())
for _ in range(n):
    a,b=input().split()
    u.merge(a,b)
s=list(input())
sc=''
for e in s:
    sc+=u.find(e)
t=list(input())
tc=''
for e in t:
    tc+=u.find(e)
print('Yes' if sc==tc else 'No')