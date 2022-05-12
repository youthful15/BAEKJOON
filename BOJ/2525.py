a, b = map(int, input().split())
c = int(input())

d = ((c + b) // 60 + a) % 24
e = (c + b) % 60

print(d, e)