a, b= map(int, input().split())

for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break
    
c = max(a, b)
    
for i in range(c, 999999999999999, c):
    if i % a == 0 and i % b == 0:
        print(i)
        break