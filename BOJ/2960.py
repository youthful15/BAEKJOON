a, b = map(int, input().split())
cnt = 0

lst = [True for i in range(a + 1)]
lst[0], lst[1] = False, False

for i in range(a + 1):
    if lst[i]:
        for j in range(i, a + 1, i):
            if lst[j]:
                lst[j] = False
                cnt += 1
            if cnt == b:
                print(j)
                break
    