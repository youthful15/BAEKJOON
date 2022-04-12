d, h, w = map(int, input().split())

ans1 = (d ** 2 / (h ** 2 + w ** 2) * (h ** 2)) ** 0.5 // 1
ans2 = (d ** 2 / (h ** 2 + w ** 2) * (w ** 2)) ** 0.5 // 1

print(int(ans1), int(ans2))