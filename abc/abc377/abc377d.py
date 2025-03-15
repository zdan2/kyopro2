n, m = map(int, input().split())
lr = [tuple(map(int, input().split())) for _ in range(n)]

# Sort intervals by L_i in decreasing order
lr.sort(reverse=True)

# Initialize variables
total_intervals = m * (m + 1) // 2  # Total number of intervals
min_Ri = m + 1
total_overlap = 0
prev_Li = m + 1

# Index for intervals
i = 0

# Collect unique L_i values in decreasing order
unique_Li = sorted(set(Li for Li, Ri in lr), reverse=True)
unique_Li.append(0)  # Append 0 to handle l from the smallest L_i down to 1

# Process intervals
for Li in unique_Li:
    num_l = prev_Li - Li  # Number of l values in the range
    # Update min_Ri for intervals where L_i >= current Li
    while i < n and lr[i][0] >= Li:
        min_Ri = min(min_Ri, lr[i][1])
        i += 1
    # If min_Ri is within bounds
    if min_Ri <= m:
        max_l = max(Li, min_Ri)
        # Number of intervals that fully contain any [L_i, R_i]
        num_intervals = num_l * (m - max_l + 1)
        total_overlap += num_intervals
    prev_Li = Li

# The answer is total intervals minus overlapping intervals
answer = total_intervals - total_overlap
print(answer)
