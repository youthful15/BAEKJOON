n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr2 = [[0] for _ in range(n)]

for i in range(n):
    p = 0
    for j in range(m):
        p += arr[i][j]
        arr2[i].append(p)

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    ans = 0
    
    for t in range(i - 1, x):
        ans += arr2[t][y] - arr2[t][j - 1]
        
    print(ans)