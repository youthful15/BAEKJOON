r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
sheep = wolf = 0
dt = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(r):
    for j in range(c):
        s = w = 0
        if arr[i][j] != '#':
            lst = [(i, j)]

            while lst:
                a, b = lst.pop()
                if arr[a][b] == 'o':
                    s += 1
                    arr[a][b] = '#'
                elif arr[a][b] == 'v':
                    w += 1
                    arr[a][b] = '#'
                elif arr[a][b] == '.':
                    arr[a][b] = '#'

                for (da, db) in dt:
                    if 0 <= a + da < r and 0 <= b + db < c and arr[a + da][b + db] != '#':
                        lst.append((a + da, b + db))

        if s > w:
            sheep += s
        else:
            wolf += w

print(sheep, wolf)
