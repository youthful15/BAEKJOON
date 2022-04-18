n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
dt = [[1, 0], [0, 1], [-1, 0], [0, -1]]
ans_lst = []

for i in range(n):
    for j in range(n):
        lst = []
        ans = 0
        if arr[i][j]:
            lst.append([i, j])
            arr[i][j] = 0
            ans += 1
            
            while lst:
                t, k = lst.pop()
                for di, dj in dt:
                    ni, nj = t + di, k + dj
                    if 0 <= ni < n and 0 <= nj < n and arr[ni][nj]:
                        arr[ni][nj] = 0
                        ans += 1
                        lst.append([ni, nj])
        
        if ans:
            ans_lst.append(ans)
            
print(len(ans_lst))
for i in sorted(ans_lst):
    print(i)                            