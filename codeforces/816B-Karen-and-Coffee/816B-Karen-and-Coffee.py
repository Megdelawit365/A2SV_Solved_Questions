n, k, q = map(int, input().split())
recs = []
qs = []
for _ in range(n):
    recs.append(list(map(int, input().split())))
for _ in range(q):
    qs.append(list(map(int, input().split())))


prefix = [0]*(200001)
admissible = [0]*(200001)
for r in recs:
    prefix[r[0]] += 1
    if r[1] < len(prefix)-1:
        prefix[r[1]+1] -= 1
for i in range(1, len(prefix)):
    prefix[i] += prefix[i-1]
for i in range(len(admissible)):
    if prefix[i] >= k:
        admissible[i] = 1
    else:
        admissible[i] = 0
for i in range(1, len(admissible)):
    admissible[i] += admissible[i-1]
    # 1 2 3 4
    # 1 2 3 4
for q in qs:
    if q[0] == 0:
        print(admissible[q[1]])
    else:
        print(str(admissible[q[1]] - admissible[q[0]-1]))