a, b = map(int, input().split())
lst = [list(map(int, input())) for _ in range(a)]
lst[0][0] = 0

a -= 1
b -= 1
dt = [[1, 0], [0, 1], [-1, 0], [0, -1]]
cnt = stop = 0

now = [[0, 0]]

while now:
    new = []
    for x, y in now:
        if x == a and y == b:
            stop = 1
            break
        for dx, dy in dt:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= a and 0 <= ny <= b:
                if lst[nx][ny]:
                    lst[nx][ny] = 0
                    new.append([nx, ny])
    cnt += 1
    now = new
    if stop:
        break

print(cnt)