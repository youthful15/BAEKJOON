n = int(input())

h1, h2 = map(int, input().split())
lst = [[] for _ in range(n + 1)]
v = [0] * (n + 1)

for _ in range(int(input())):
    a, b = map(int, input().split())

    lst[a].append(b)
    lst[b].append(a)

now_lst = lst[h1]
v[h1] = 1
find = 0
ans = 0

while now_lst:

    new_lst = []

    for num in now_lst:
        if num == h2:
            find = 1
        v[num] = 1
        for new in lst[num]:
            if v[new] == 0:
                v[new] = 1
                new_lst.append(new)

    ans += 1
    now_lst = new_lst

    if find:
        break

if find:
    print(ans)
else:
    print(-1)
