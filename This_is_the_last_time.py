t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    casinos = []
    for _ in range(n):
        casinos.append(list(map(int, input().split())))
    casinos = sorted(casinos, key=lambda x: x[0])
    for c in casinos:
        if c[0] <= k <= c[1]:
            if c[2] > k:
                k = c[2]
    print(k)
