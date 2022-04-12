import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
arr = [0]

for num in lst:
    arr.append(arr[-1] + num)

for _ in range(m):
    a, b = map(int, input().split())
    print(arr[b] - arr[a - 1])