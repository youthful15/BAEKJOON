import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
lst = [input() for _ in range(n)]

for _ in range(m):
    a = input()
    if a in lst:
        print(lst.index(a) + 1)
    else:
        print(lst[int(a) - 1])