n, r, c = map(int, input().split())

if r // 4 and c // 4

# if r < 2 ** n / 2 and c < 2 ** n / 2:  # 좌상
#     print(r // 2 * 2 ** n + c // 2 * 4 + r % 2 * 2 + c % 2)
# elif c < 2 ** n / 2:  # 좌하
#     r -= 2 ** (n - 1)
#     print(int(r // 2 * 2 ** n + c // 2 * 4 + r %
#           2 * 2 + c % 2 + (2 ** n) ** 2 * 0.5))
# elif r < 2 ** n / 2:  # 우상
#     c -= 2 ** (n - 1)
#     print(int(r // 2 * 2 ** n + c // 2 * 4 + r %
#           2 * 2 + c % 2 + (2 ** n) ** 2 * 0.25))
# else:  # 우하
#     c -= 2 ** (n - 1)
#     r -= 2 ** (n - 1)
#     print(int(r // 2 * 2 ** n + c // 2 * 4 + r %
#           2 * 2 + c % 2 + (2 ** n) ** 2 * 0.75))
