n = int(input())
m = int(input())

tas = input()
c = 'I' + 'OI' * n
ans = 0

# 자리수 2n - 1

for i in range(m - 2 * n - 1):
    if tas[i:i + 2 * n + 1] == c:
        ans += 1
        
print(ans)