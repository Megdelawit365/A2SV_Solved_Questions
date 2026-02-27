t = int(input())
for _ in range(t):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if arr1[i] > arr2[i]:
            arr1[i], arr2[i] = arr2[i], arr1[i]
            ans.append(f"3 {i+1}")

    for i in range(n):
        for j in range(n-1):
            if arr1[j] > arr1[j+1]:
                arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
                ans.append(f"1 {j+1}")
    for i in range(n):
        for j in range(n-1):
            if arr2[j] > arr2[j+1]:
                arr2[j], arr2[j+1] = arr2[j+1], arr2[j]
                ans.append(f"2 {j+1}")
    print(len(ans))
    for a in ans:
        print(a)
