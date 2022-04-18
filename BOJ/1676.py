n = int(input())
ans = 1
cnt = 0

for i in range(2, n + 1):
    ans *= i
    
for j in str(ans)[::-1]:
    if j == '0':
        cnt += 1
    else:
        break
    
print(cnt)