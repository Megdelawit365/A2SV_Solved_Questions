n, k = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0
if k == 1:
    print(nums[-1] - nums[0])
    exit()
if k == n:
    print(0)
    exit()
gaps = []
for i in range(1, n):
    gaps.append(nums[i]-nums[i-1])
gaps.sort(reverse=True)
ans = sum(gaps)
ans -= sum(gaps[0:k-1])
print(ans)
