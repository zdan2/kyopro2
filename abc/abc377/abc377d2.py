n, m = map(int, input().split())
lr = [tuple(map(int, input().split())) for _ in range(n)]

from collections import defaultdict

# Collect R_i's for each L_i
L_to_R = defaultdict(list)
unique_L = set()

for L_i, R_i in lr:
    L_to_R[L_i].append(R_i)
    unique_L.add(L_i)

# Sort unique L_i's in decreasing order
unique_L = sorted(unique_L, reverse=True)

# Initialize variables
current_min_R = m + 1
total_valid_intervals = 0
prev_L = m + 1  # Start from M + 1 to handle the initial case

# Precompute prefix sums for quick sum calculation
def prefix_sum(k):
    return k * (k + 1) // 2

for L in unique_L:
    # Update current_min_R with the minimum R_i where L_i == L
    min_R_i = min(L_to_R[L])
    current_min_R = min(current_min_R, min_R_i)

    # Define the range for l
    a = L
    b = min(current_min_R - 1, prev_L - 1)
    if a > b:
        prev_L = L
        continue

    num_terms = b - a + 1
    sum_l = prefix_sum(b) - prefix_sum(a - 1)
    total = num_terms * current_min_R - sum_l
    total_valid_intervals += total

    prev_L = L

# Handle remaining l values from 1 to prev_L - 1
a = 1
b = min(current_min_R - 1, prev_L - 1)
if a <= b:
    num_terms = b - a + 1
    sum_l = prefix_sum(b) - prefix_sum(a - 1)
    total = num_terms * current_min_R - sum_l
    total_valid_intervals += total

# Calculate total number of intervals
total_intervals = m * (m + 1) // 2

# The answer is total intervals minus the intervals that fully contain any [L_i, R_i]
answer = total_intervals - total_valid_intervals
print(answer)
n