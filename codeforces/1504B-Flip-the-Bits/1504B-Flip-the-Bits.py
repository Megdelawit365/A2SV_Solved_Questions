t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    ones = 0
    for num in a:
        if num == "1":
            ones += 1
    zeros = n - ones
    balance = zeros - ones
    flipped = False
    flag = True
    for i in range(n-1, -1, -1):
        num1 = a[i] if not flipped else str(1 - int(a[i]))
        if num1 == b[i]:
            if a[i] == "0":
                balance -= 1
            else:
                balance += 1
            continue
        if balance != 0:
            flag = False
            break
        flipped = not flipped
        if a[i] == "0":
            balance -= 1
        else:
            balance += 1
    if flag:
        print("YES")
    else:
        print("NO")