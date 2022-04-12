def dfs(x):
    for lst in arr:
        if lst[0] == x:
            print(lst[1], end = ' ')
            dfs(lst[1])
    


n, m, v = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
arr = sorted(arr, key = lambda x : x[1])

dfs(v)

