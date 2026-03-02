n, s = map(int, input().split())
nums = list(map(int, input().split()))
maxLen = 0
left = 0
currSum = 0
for right in range(n):
    currSum += nums[right]
    while currSum > s:
        currSum -= nums[left]
        left += 1
    maxLen = max(maxLen, right-left+1)
print(maxLen)
