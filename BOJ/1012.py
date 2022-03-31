for tc in range(int(input())):
    m, n, k = map(int, input().split())
    arr = [[0] * n for _ in range(m)]
    
    for _ in range(k):
        a, b = map(int, input().split())
        arr[a][b] = 1
        
    ans = 0
    
    for i in range(m):
        for j in range(n):
            if arr[i][j]:
                ans += 1
                lst = [[i, j]]
                while lst:
                    x, y = lst.pop()
                    arr[x][y] = 0
                    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and arr[nx][ny]:
                            arr[nx][ny] = 0
                            lst += [[nx, ny]]
    
    print(ans)