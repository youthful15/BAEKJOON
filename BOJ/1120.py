a, b = input().split()
ans = 50

if len(b) < len(a):
    a, b = b, a

for i in range(len(b) - len(a) + 1):
    temp = 0
    for j in range(len(a)):
        if a[j] != b[i + j]:
            temp += 1
    if temp < ans:
        ans = temp

print(ans)
