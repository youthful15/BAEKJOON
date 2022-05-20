import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [int(input()) for i in range(m)]
ans = 0
num = 0

lst.sort(reverse=True)

for i in range(min(n, m)):
    if ans < lst[i] * (i + 1):
        ans = lst[i] * (i + 1)
        num = lst[i]

print(num, ans)
