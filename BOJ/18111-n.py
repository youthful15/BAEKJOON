n, m, b = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

s = answer = 0
for mini in lst:
    s += sum(mini)
    
s = round(s / (n * m))

for i in range(n):
    for j in range(m):
        if lst[i][j] > s:
            answer += (lst[i][j] - s) * 2
        elif lst[i][j] < s:
            answer += (s - lst[i][j])

print(f'{answer} {s}')