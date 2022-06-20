import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
dict = {}

# for i in range(n):
#     dict[i] = input().rstrip()
lst = [input() for _ in range(n)]

for _ in range(m):
    a = input()
    try:
        print(lst[int(a) - 1])
    except:
        print(lst.index(a) + 1)
