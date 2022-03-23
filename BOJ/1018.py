n, m = map(int, input().split())
lst = [list(input()) for _ in range(n)]

ans = 64

w = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']] * 4
b = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']] * 4

for i in range(8):
    if i % 2:
        w += ['B']
        b += ['W']
    else:
        w += ['W']
        b += ['B']
        
for i in range(n - 7):
    for j in range(m - 7):
        w_start = b_start = 0
        for h in range(8):
            for x in range(8):
                if lst[i + h][j + x] != w[h][x]:
                    w_start += 1
                elif lst[i + h][j + x] != b[h][x]:
                    b_start += 1
        if ans > w_start:
            ans = w_start
        if ans > b_start:
            ans = b_start
            
print(ans)
