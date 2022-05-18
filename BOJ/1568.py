a = int(input())

ans = 0
bird = 0

while a != bird:
    for i in range(1, 10 ** 9):
        if a < i:
            break
        ans += 1
        a -= i

print(ans)
