words = list(input())
ans = 0

for word in words:
    ans += (ord(word) - 62) // 3 + 2
    if word == 'S' or word == 'V' or word == 'Y' or word == 'Z':
        ans -= 1
    
print(ans)