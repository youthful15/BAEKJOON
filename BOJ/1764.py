n, m = map(int, input().split())
lst = [input() for _ in range(n)]
lst2 = [input() for _ in range(m)]

ans = set(lst) & set(lst2)
ans = sorted(list(ans))

print(len(ans))
for _ in range(len(ans)):
    print(ans[_])