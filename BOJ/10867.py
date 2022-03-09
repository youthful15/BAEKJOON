a = int(input())
lst = list(map(int, input().split()))

a = sorted(list(set(lst)))

print(*a)