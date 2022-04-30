a, b = map(int, input().split())

while a != 0 or b != 0:
    arr = [list(map(int, input().split())) for _ in range(b)]
    ans = 0
    
    for i in range(b):
        for j in range(a):
            if arr[i][j]:
                arr[i][j] = 0
                lst = [[i, j]]
                while lst:
                    x, y = lst.pop()
                    for dx, dy in ([1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < b and 0 <= ny < a and arr[nx][ny]:
                            arr[nx][ny] = 0
                            lst.append([nx, ny])
                ans += 1
                
    print(ans)
    a, b = map(int, input().split())