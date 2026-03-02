n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
left = 0
currSum = 0
for right in range(n):
    currSum += arr[right]
    while currSum >= s:
        ans += (n-right)
        currSum -= arr[left]
        left += 1
print(ans)
