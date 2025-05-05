from collections import deque
nums=[1,2,3,4,5]
target=6

q=deque()
q.append(([],0))
q.append(([1],0))
a=[]
while q:
    v,i=q.popleft()
    if i+1>=len(nums):
        continue
    if sum(v)+nums[i+1]==target:
        a.append(v+[nums[i+1]])
    elif sum(v)+nums[i]<target:
        q.append((v+[nums[i+1]],i+1))
        q.append((v,i+1))
print(a)