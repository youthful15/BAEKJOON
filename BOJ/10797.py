a = int(input())
lst = list(map(int, input().split()))

print(lst.count(a % 10))