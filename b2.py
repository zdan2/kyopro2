nums = [1, 2, 3, 4, 5]
target = 6
a = []

def rec(v, i):
    if i + 1 >= len(nums):
        return
    if sum(v) + nums[i+1] == target:
        a.append(v + [nums[i+1]])
    elif sum(v) + nums[i] < target:
        rec(v + [nums[i+1]], i + 1)
        rec(v, i + 1)
rec([], 0)
rec([1], 0)

print(a)