n = int(input())
num = [input() for _ in range(n)]
lst = [0] * (n)
ans = 0
j = len(num[0]) - 1

while True:

    for i in range(n):
        lst[i] = num[i][j:]

    j -= 1

    if len(set(lst)) == len(lst):
        break

print(len(lst[0]))
