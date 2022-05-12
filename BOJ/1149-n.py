

n = int(input())
r, g, b = map(int, input().split())
ans = [[r, 0], [g, 1], [b, 2]]

for x in range(n - 1):
    new_ans = []
    r, g, b = list(map(int, input().split()))

    for (num, color) in ans:
        if color == 0:
            new_ans.append([num + g, 1])
            new_ans.append([num + b, 2])
        elif color == 1:
            new_ans.append([num + r, 0])
            new_ans.append([num + b, 2])
        else:
            new_ans.append([num + r, 0])
            new_ans.append([num + g, 1])

    ans = new_ans

min = ans[0][0]

for (num, color) in ans:
    if num < min:
        min = num

print(min)
