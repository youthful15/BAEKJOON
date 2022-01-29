a = int(input())

for i in range(a):
    b = list(map(int, str(i)))
    if i + sum(b) == a:
        print(i)
        break
else:
    print(0)
    