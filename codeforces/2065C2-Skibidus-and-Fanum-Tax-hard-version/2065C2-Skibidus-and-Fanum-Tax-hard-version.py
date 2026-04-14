import bisect
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort()
    prev = float('-inf')
    flag = True

    for i in range(n):
        op1 = a[i] if a[i] >= prev else float('inf')

        j = bisect.bisect_left(b, prev + a[i])
        if j < m:
            op2 = b[j] - a[i]
        else:
            op2 = float('inf')

        best = min(op1, op2)

        if best == float('inf'):
            flag = False
            break

        prev = best

    print("YES" if flag else "NO")