def find(i, j, a, c):
    global arr, sett
    dt = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    if c == 6:
        sett.add(a)
        return

    for (di, dj) in dt:
        if 0 <= di + i < 5 and 0 <= dj + j < 5:
            find(di + i, dj + j, a + chr(arr[di + i][dj + j]), c + 1)


arr = [list(map(int, input().split())) for _ in range(5)]
sett = set([])
dt = [[1, 0], [0, 1], [-1, 0], [0, -1]]

for i in range(5):
    for j in range(5):
        for (di, dj) in dt:
            if 0 <= di + i < 5 and 0 <= dj + j < 5:
                find(di + i, dj + j, chr(arr[i][j]
                                         ) + chr(arr[di + i][dj + j]), 2)

print(len(sett))
