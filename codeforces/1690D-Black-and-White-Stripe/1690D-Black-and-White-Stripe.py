t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    maxNum, left, currNum = 10**10, 0, 0
    for right in range(n):
        if s[right] == "B":
            currNum += 1
        if right - left + 1 == k:
            maxNum = min(maxNum, k-currNum)
            if s[left] == "B":
                currNum -= 1
            left += 1
    print(maxNum)