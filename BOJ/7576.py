m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
lst = []
new_lst = []
ans = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            lst.append([i, j])
            
dt = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while lst:
    for y, x in lst:
        for dy, dx in dt:
            ny, nx = dy + y, dx + x
            if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] == 0:
                arr[ny][nx] = 1
                new_lst.append([ny, nx])
    ans += 1
    lst = new_lst
    new_lst = []

for l in arr:
    if 0 in l:
        print('-1')
        break
else:
    print(ans - 1)