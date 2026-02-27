from collections import Counter
n = int(input())
for _ in range(n):
    s = input()
    t = input()
    count1 = Counter(s)
    count2 = Counter(t)
    flag = True
    for k, v in count1.items():
        if count2[k] < v:
            flag = False
        count2[k] -= v
    if not flag:
        print("Impossible")
        continue
    ans = ""
    for k, v in count2.items():
        ans += k*v
    ans = "".join(sorted(ans))

    i, j = 0, 0
    while j < len(ans) and i < len(s):
        if s[i] <= ans[j]:
            sub1 = ans[:j]
            sub2 = ans[j:]
            ans = sub1 + s[i] + sub2
            i += 1
        j += 1
    while i < len(s):
        ans += s[i]
        i += 1
    print(ans)

# babadab
# abacabadabacaba
# aaaaa b cc
