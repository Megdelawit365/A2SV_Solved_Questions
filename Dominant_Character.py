from collections import Counter
n = int(input())
valid = ["aa", "aba", "aca", "abca", "acba", "abbacca", "accabba"]
for _ in range(n):
    length = int(input())
    s = input()
    flag = False
    for v in valid:
        if v in s:
            print(len(v))
            flag = True
            break
    if not flag:
        print(-1)
