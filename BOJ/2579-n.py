import sys
input = sys.stdin.readline

def stair(i, n, s):
    global ans, a
    
    if i == a:
        s += lst[i]
        if s > ans:
            ans = s
    elif i < a:
        s += lst[i]
        if n + 1 <= 2:
            stair(i + 1, n + 1, s)
        if i + 2 <= a:
            stair(i + 2, 0, s)


a = int(input())
lst = [int(input()) for _ in range(a)] + [0]
ans = 0

stair(0, 0, 0)
print(ans)