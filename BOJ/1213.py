a = input()
lst = [0 for _ in range(26)]
ans = ''
temp = 0

for alpha in a:
    lst[ord(alpha) - 65] += 1

if len(a) % 2:
    for i in range(len(lst)):
        if lst[i] % 2:
            temp += 1
            center = chr(65 + i)
            if temp >= 2:
                print("I'm Sorry Hansoo")
                break
        if lst[i] // 2:
            ans += chr(65 + i) * (lst[i] // 2)
    else:
        print(ans + center + ans[::-1])

else:
    for i in range(len(lst)):
        if lst[i] % 2:
            print("I'm Sorry Hansoo")
            break
        if lst[i] // 2:
            ans += chr(65 + i) * (lst[i] // 2)
    else:
        print(ans + ans[::-1])
