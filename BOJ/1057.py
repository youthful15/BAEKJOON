n, a, b = map(int, input().split())

if a > b:
    a, b = b, a
    
ans = 1

while True:
    if b - 1 == a and a % 2:
        break
    a, b = (a + 1) // 2 , (b + 1) // 2
    ans += 1
    
print(ans)