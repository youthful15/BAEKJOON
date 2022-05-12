a, b = map(int, input().split())

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

print(a + b - len(set(lst1) & set(lst2)) * 2)
