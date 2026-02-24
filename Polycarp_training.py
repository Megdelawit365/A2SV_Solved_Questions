from collections import Counter
n = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)
ans = 0
num = 1
idx = 0
while idx < n:
    if nums[idx] >= num:
        ans += 1
        num += 1
    idx += 1
print(ans)
