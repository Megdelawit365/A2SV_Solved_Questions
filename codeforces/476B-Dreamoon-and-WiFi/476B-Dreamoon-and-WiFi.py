def solve():
    s1 = list(input())
    s2 = list(input())

    sum1, sum2 = 0, 0
    n = 0
    total = 0
    correct = 0

    for i, j in zip(s1, s2):
        if i == "+":
            sum1 += 1
        else:
            sum1 -= 1

        if j == "+":
            sum2 += 1
        elif j == "?":
            n += 1
        else:
            sum2 -= 1

    if n == 0:
        print(format(1, ".12f") if sum1 == sum2 else format(0, ".12f"))
        return

    def build(path, count):
        nonlocal total, correct

        if len(path) == n:
            total += 1
            if count + sum2 == sum1:
                correct += 1
            return

        path.append("+")
        build(path, count + 1)
        path.pop()

        path.append("-")
        build(path, count - 1)
        path.pop()

    build([], 0)

    print(format(correct / total, ".12f"))


solve()