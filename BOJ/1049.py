n, m = map(int, input().split())
min_set, min_one = map(int, input().split())

for i in range(m - 1):
    a, b = map(int, input().split())
    if a < min_set:
        min_set = a
    if b < min_one:
        min_one = b

if min_one * 6 <= min_set:
    print(min_one * n)
else:
    print(min((n // 6) * min_set + (n % 6) * min_one, (n // 6 + 1) * min_set))