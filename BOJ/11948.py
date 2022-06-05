lst = [0] * 4
lst[0] = int(input())
lst[1] = int(input())
lst[2] = int(input())
lst[3] = int(input())

a = int(input())
b = int(input())

print(sum(lst) - min(lst) + max(a, b))
