for i in range(3):
    a, b, c, d, e, f = map(int, input().split())
    ans = (d * 3600 + e * 60 + f) - (a * 3600 + b * 60 + c)

    h = ans // 3600
    m = (ans % 3600) // 60
    s = ((ans % 3600) % 60)

    print(h, m, s)
