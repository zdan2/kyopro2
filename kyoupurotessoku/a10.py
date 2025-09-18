def find_n(a, k):
    low, high = 1, max(a)*k 
    while low < high:
        mid = (low + high) // 2
        total = sum(mid // ai for ai in a) 
        if total >= k:
            high = mid 
        else:
            low = mid + 1 
    return low

n,k=map(int,input().split())
a = list(map(int,input().split()))
result = find_n(a, k)
print(result)
