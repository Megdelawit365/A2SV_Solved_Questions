# 13 22
# 11 22
# 654 321
# 4443
# same numbber  of colors in left and right
# equal number of left and right
#  4443
from collections import Counter
t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    socks = list(map(int, input().split()))
    countLeft = Counter(socks[0:l])
    countRight = Counter(socks[l:])

    for k, v in countLeft.items():
        if k in countRight:
            equal = min(v, countRight[k])
            countLeft[k] -= equal
            countRight[k] -= equal

    left, right = sum(countLeft.values()), sum(countRight.values())

    if left < right:
        countRight, countLeft = countLeft, countRight
        left, right = right, left

    ans = 0
    flipsNeeded = abs(left - right)//2

    for k, v in countLeft.items():
        while countLeft[k] >= 2 and flipsNeeded > 0:
            flipsNeeded -= 1
            countLeft[k] -= 2
            ans += 1
    ans += flipsNeeded
    ans += (sum(countLeft.values()) + sum(countRight.values()))//2
    print(ans)

# 50min
