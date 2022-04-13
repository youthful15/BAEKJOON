n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
g = s = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'X':
            break
    else:
        g += 1
        
for i in range(m):
    for j in range(n):
        if arr[j][i] == 'X':
            break
    else:
        s += 1
        
print(max(g, s))