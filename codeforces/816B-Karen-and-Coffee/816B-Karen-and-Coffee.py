# 1 2 3 4
    # 1 2 3 4
for q in qs:
    if q[0] == 0:
        print(admissible[q[1]])
    else:
        print(str(admissible[q[1]] - admissible[q[0]-1]))