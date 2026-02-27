t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    if n == 2:
        print(n)
        print(" ".join([str(i) for i in nums]))
        continue
    subseq = [nums[0]]
    for i in range(1, n-1):
        if (nums[i] > nums[i-1]) != (nums[i+1] > nums[i]):
            subseq.append(nums[i])
    subseq.append(nums[-1])

    print(len(subseq))
    print(" ".join([str(i) for i in subseq]))
