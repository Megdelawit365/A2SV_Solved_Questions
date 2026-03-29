s = input()
stack = [-1]
max_len = 0
count = 0
for i, char in enumerate(s):
    if char == "(":
        stack.append(i)
    else:
        j = stack.pop()
        if not stack:
            stack.append(i)
        else:
            length = i - stack[-1]
            if length > max_len:
                max_len = length
                count = 1
            elif length == max_len:
                count += 1

if max_len == 0:
    print("0 1")
else:
    print(f"{max_len} {count}")

# the reason we add -1 at the front of the stack is because ()() and ()(()) are  Regular Bracket Sequences, not () and () separately.