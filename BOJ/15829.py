a = int(input())
b = list(input())
ans = 0

for i in range(len(b)):
    ans += (ord(b[i]) - 96) * 31 ** i
    
print(ans % 1234567891)