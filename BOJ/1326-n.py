import sys
sys.setrecursionlimit(10 ** 9)


def dfs(now, cnt):
    global lst, b, ans
    if cnt >= ans:
        return
    elif now == b:
        if cnt < ans:
            ans = cnt
        return

    i = 1
    while now + lst[now] * i <= len(lst) - 1:
        if v[now + lst[now] * i] == 0:
            v[now + lst[now] * i] = 1
            dfs(now + lst[now] * i, cnt + 1)
            v[now + lst[now] * i] = 0
        i += 1

    i = 1
    while now - (lst[now] * i) >= 0:
        if v[now - (lst[now] * i)] == 0:
            v[now - (lst[now] * i)] = 1
            dfs(now - (lst[now] * i), cnt + 1)
            v[now - (lst[now] * i)] = 0
        i += 1


n = int(input())
lst = list(map(int, input().split()))
v = [0] * n
a, b = map(int, input().split())
a, b = a - 1, b - 1
ans = 10000

v[a] = 1
dfs(a, 0)

if ans != 10000:
    print(ans)
else:
    print(-1)
