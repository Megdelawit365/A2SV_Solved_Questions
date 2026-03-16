t = int(input())
for _ in range(t):
    n = int(input())
    red = list(map(int, input().split()))
    m = int(input())
    blue = list(map(int, input().split()))
    for i in range(1, n):
        red[i] = red[i] + red[i-1]
    for i in range(1, m):
        blue[i] = blue[i] + blue[i-1]

    print(max(max(red), 0) + max(max(blue), 0))