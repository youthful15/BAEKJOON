a = int(input())
lst = [list(map(int, input().split())) for _ in range(a)]

lst = sorted(lst, key=lambda x: x[2])

print(lst)

print(lst[-1][0], lst[-1][1])
print(lst[-2][0], lst[-2][1])

i = -3

if lst[-1][0] == lst[-2][0]:
    while lst[i][0] == lst[-1][0]:
        i -= 1

print(lst[i][0], lst[i][1])
