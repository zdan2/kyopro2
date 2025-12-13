class Node:
    def __init__(self,num):
        self.num=num
        self.left=None
        self.right=None

class Tree:
    def __init__(self,node):
        self.head=node
    
    def add(self, node):
        val = node.num
        current = self.head
        
        while True:
            if val > current.num:
                if current.right is None:
                    current.right = node
                    break
                current = current.right
            else:
                if current.left is None:
                    current.left = node
                    break
                current = current.left 
n=int(input())
a=list(map(int,input().split()))
root=Node(a[0])
tree=Tree(root)
for e in a[1:]:
    tree.add(Node(e))
r=[]
def dfs(tree,cur):
    if cur is None:
        return
    r.append(cur.num)
    dfs(tree,cur.left)
    dfs(tree,cur.right)

dfs(tree,root)
d={}
for i in range(n):
    d[r[i]]=i+1
m=int(input())
b=list(map(int,input().split()))
for e in b:
    if e not in d:
        print(-1)
    else:
        print(d[e])