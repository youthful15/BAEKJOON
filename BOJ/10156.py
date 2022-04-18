k, n, m = map(int, input().split())

if (m - k * n) < 0:
    print(k * n - m)
else:
    print(0)    