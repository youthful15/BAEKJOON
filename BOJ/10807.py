n = int(input())
lst = list(map(int, input().split()))
v = int(input())

ans = 0
for n in lst:
    if n == v:
        ans += 1
print(ans)
