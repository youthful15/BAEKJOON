n = int(input())
dict = {}
lst = []

for _ in range(n):
    a = input()
    if a[0] not in dict:
        dict[a[0]] = 1
    else:
        dict[a[0]] += 1

for key in dict:
    if dict[key] >= 5:
        lst.append(key)

if not lst:
    print('PREDAJA')
else:
    lst.sort()
    for a in lst:
        print(a, end='')
