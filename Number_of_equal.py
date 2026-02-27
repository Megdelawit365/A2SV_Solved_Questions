n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
i, j = 0, 0
ans = 0
while i < n and j < m:
    if arr1[i] < arr2[j]:
        i += 1
    elif arr1[i] > arr2[j]:
        j += 1
    else:
        count1, count2 = 0, 0
        num = arr1[i]
        while i < n and arr1[i] == num:
            count1 += 1
            i += 1
        while j < m and arr2[j] == num:
            count2 += 1
            j += 1
        ans += count1 * count2
print(ans)
