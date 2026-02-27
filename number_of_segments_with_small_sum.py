n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
j = 0
_sum = 0
for i in range(n):
    while j < n and _sum + arr[j] <= s:
        _sum += arr[j]
        j += 1
    ans += j - i
    _sum -= arr[i]
print(ans)
