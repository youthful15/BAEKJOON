n, k = map(int, input().split())
ans = 0
lst = []

for i in range(1, n + 1):
    if n % i == 0:
        lst += [i]

ans = 0 if len(lst) < k else lst[k - 1]
print(ans)