# leaf = [False] * (n+1)

# for c in children:
#     if len(c) > 0:
#         leaf[c] = True

ans = "Yes"
for child in children:
    if not child:
        continue
    count = 0
    for c in child:
        if len(children[c]) == 0:
            count += 1
    if count < 3:
        ans = "No"

print(ans)