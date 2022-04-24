from re import I


a = int(input())

b = 0
i = 1

while True:
    b += i
    if b >= a:
        break
    i += 1

if a % b:
    print(f'{a % i}/{i - a % i + 1}')
else:
    print(f'{i}/1')