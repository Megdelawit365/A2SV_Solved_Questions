from collections import defaultdict
n, k = map(int, input().split())
nums = list(map(int, input().split()))
left = 0
idx1, idx2 = 0, 0
count = defaultdict(int)
for right in range(n):
    count[nums[right]] += 1
    while len(count) > k:
        count[nums[left]] -= 1
        if count[nums[left]] == 0:
            del count[nums[left]]
        left += 1
    if len(count) <= k:
        if (idx2 - idx1) < (right - left + 1):
            idx1 = left
            idx2 = right
print(f"{idx1 + 1} {idx2 + 1}")