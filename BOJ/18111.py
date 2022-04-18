import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

ans = 2 ** 99
high = 0

for b in range(0, 257):
    temp = 0
    block = t
    
    for i in range(n):
        for j in range(m):
            if b > lst[i][j]:
                temp += b - lst[i][j]
                block -= b - lst[i][j]
            elif b < lst[i][j]:
                temp += (lst[i][j] - b) * 2
                block += lst[i][j] - b
                
    if block >= 0 and temp <= ans:
        ans = temp
        high = b
    elif block < 0:
        break
    
print(ans, high)