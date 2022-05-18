def find(s, h, i):
    global n, ans
    if s <= 0:
        return
    if i == n:
        if ans < h:
            ans = h
        return

    find(s - sta_lst[i], h + hap_lst[i], i + 1)
    find(s, h, i + 1)


n = int(input())
ans = 0
sta_lst = list(map(int, input().split()))
hap_lst = list(map(int, input().split()))

find(100, 0, 0)

print(ans)
