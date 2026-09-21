def calc_cumulative_sum(arr,k):
    cum_sum = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        if cum_sum[i]==0:
            cum_sum[i+1]=arr[i]%k
        else:
            cum_sum[i + 1] = (cum_sum[i] + arr[i])%k
    return cum_sum
n,k=map(int,input().split())
a=list(map(int,input().split()))
ma=max(a)
for i in range(5):
    print(a)
    a=calc_cumulative_sum(a,k)[1:]

    