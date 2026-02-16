row, col = -1, 0
for _ in range(5):
    row += 1
    string = input()
    string = "".join(string.split())
    flag = False
    for i, s in enumerate(string):
        if s == "1":
            col = i
            flag = True
            break
    if flag:
        break
ans = abs(2-row) + abs(2-col)
print(ans)
