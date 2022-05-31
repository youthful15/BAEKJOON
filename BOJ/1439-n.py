a = input()
ans = 0

for i in range(len(a) - 1):
    if a[i + 1] != a[i]:
        ans += 1

if a[-1] != a[-2]:
    ans += 1

print(ans // 2)
