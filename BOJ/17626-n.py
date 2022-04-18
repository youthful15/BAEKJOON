import math

n = int(input())
ans = 0

while n != 0:
    b = math.floor(n ** 0.5)
    n -= b ** 2
    ans += 1
    
print(ans)