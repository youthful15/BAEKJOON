lst = [list(map(int, input().split())) for i in range(3)]
ave = 0
answer = []

for j in range(2):
    if lst[0][j] == lst[1][j]:
        a = lst[2][j]
    elif lst[0][j] == lst[2][j]:
        a = lst[1][j]
    else:
        a = lst[0][j]
    answer += [a]
    
print(*answer)