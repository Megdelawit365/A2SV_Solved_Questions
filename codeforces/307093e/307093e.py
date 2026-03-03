from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
count = defaultdict(int)
ans = 0

for right in range(n):
    count[arr[right]] += 1
    while len(count) > k:
        # print(arr[left])
        count[arr[left]] -= 1
        if count[arr[left]] == 0:
            del count[arr[left]]
        left += 1
    ans += right - left + 1
print(ans)