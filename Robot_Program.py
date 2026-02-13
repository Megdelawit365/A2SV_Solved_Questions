t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split(" "))
    commands = input()
    preLoop = 0
    while preLoop < n:
        if commands[preLoop] == "L":
            x -= 1
        elif commands[preLoop] == "R":
            x += 1
        preLoop += 1
        if x == 0:
            break
    if preLoop == n and x != 0:
        print(0)
        continue
    loop = 0
    while loop < n:
        if commands[loop] == "L":
            x -= 1
        elif commands[loop] == "R":
            x += 1
        loop += 1
        if x == 0:
            break
    if loop == n and x != 0:
        print(1)
        continue
    if loop == 0:
        print("loop 0")
        continue
    print((k - preLoop)//loop + 1)
