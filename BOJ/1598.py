a, b = map(int, input().split())

if a < b:
    a, b = b, a
    
print((a - 1) // 4 - (b - 1) // 4 + abs((a - 1) % 4 - (b - 1) % 4))