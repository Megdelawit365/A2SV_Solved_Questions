h, w = map(int, input().split())
hor = [[0]*(w+1) for _ in range(h+1)]
ver = [[0]*(w+1) for _ in range(h+1)]
s = []
for i in range(h):
    s.append(input())

for i in range(h):
    for j in range(w-1):
        if s[i][j] == "." and s[i][j+1] == ".":
            hor[i+1][j+1] = 1

for i in range(h-1):
    for j in range(w):
        if s[i][j] == "." and s[i+1][j] == ".":
            ver[i+1][j+1] = 1

for i in range(1, h+1):
    for j in range(1, w+1):
        top = hor[i-1][j]
        left = hor[i][j-1]
        topLeft = hor[i-1][j-1]
        hor[i][j] = top + left + hor[i][j] - topLeft

for i in range(1, h+1):
    for j in range(1, w+1):
        top = ver[i-1][j]
        left = ver[i][j-1]
        topLeft = ver[i-1][j-1]
        ver[i][j] = top + left + ver[i][j] - topLeft


q = int(input())
for i in range(q):
    s = list(map(int, input().split()))
    row1, col1, row2, col2 = s[0], s[1], s[2], s[3]
    sum1 = hor[row2][col2-1] - hor[row1-1][col2-1] - \
        hor[row2][col1-1] + hor[row1-1][col1-1]

    sum2 = ver[row2-1][col2] - ver[row1-1][col2] - \
        ver[row2-1][col1-1] + ver[row1-1][col1-1]

    print(sum1 + sum2)