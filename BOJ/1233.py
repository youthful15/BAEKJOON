a, b, c = map(int, input().split())

dict = {}
ans_key = 0
ans_value = 0

for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            num = i + j + k
            dict[num] = 1 if num not in dict else dict[num] + 1
            num = 0
            
for a, b in dict.items():
    if b > ans_value:
        ans_value = b
        ans_key = a

print(ans_key)