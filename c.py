nums=[1,2,3]

def f(arr,s):
    if len(arr)==len(s):
        print('last',arr)
        return arr[:]
    for e in s:
        if e not in arr:
            arr.append(e)
            print(arr)
            b=arr[:]
            f(b,s)
a=[]
for e in nums:
    r=f([e],set(nums))
    a.append(r)
print(a)