a, b, n = map(int, input().split())
c = (a / b - (a // b)) * 100000000000

print(c)