n, a = map(int, input().split())

for l in range(a, 101):

    if l % 2 and n / l == int(n / l):
        if n // l - (l // 2) < 0:
            print(-1)
            break
        for i in range(n // l - (l // 2), n // l + (l // 2) + 1):
            print(i, end=' ')
        break

    elif n / l == int(n / l) + 0.5:
        if n // l - (l // 2) + 1 < 0:
            print(-1)
            break
        for i in range(n // l - (l // 2) + 1, n // l + (l // 2) + 1):
            print(i, end=' ')
        break

else:
    print(-1)
