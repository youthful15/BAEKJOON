n = int(input())
lst = list(map(int, input().split()))
arr = [0] * n
now = 1

for num in lst:
    cnt = i = 0
    while cnt != num:
        if not arr[i]:
            cnt += 1
        i += 1

    while arr[i]:
        i += 1
    arr[i] = now
    now += 1

print(*arr)
