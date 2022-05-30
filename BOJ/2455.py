ans = 0
now = 0

for i in range(4):
    a, b = map(int, input().split())
    now += b
    now -= a

    if now > ans:
        ans = now

print(ans)
