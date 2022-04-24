n, r, c = map(int, input().split())

if r < 2 ** n / 2 and c < 2 ** n / 2:
    print(r // 2 * 2 ** n + c // 2 * 4 + r % 2 * 2 + c % 2)
elif c < 2 ** n / 2:
    r -= 2 ** (n - 1)
    print(int(r // 2 * 2 ** n + c // 2 * 4 + r % 2 * 2 + c % 2 + (2 ** n) ** 2 * 0.5))
elif r < 2 ** n / 2:
    c -= 2 ** (n - 1)
    print(int(r // 2 * 2 ** n + c // 2 * 4 + r % 2 * 2 + c % 2 + (2 ** n) ** 2 * 0.25))
else:
    c -= 2 ** (n - 1)
    r -= 2 ** (n - 1)
    print(int(r // 2 * 2 ** n + c // 2 * 4 + r % 2 * 2 + c % 2 + (2 ** n) ** 2 * 0.75))