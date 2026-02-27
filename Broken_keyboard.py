t = int(input())
for _ in range(t):
    s = input()
    ans = set()
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        if (j-i) % 2 != 0:
            ans.add(s[i])
        i = j
    ans = sorted(list(ans))
    print("".join(ans))
