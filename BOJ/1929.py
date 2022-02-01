a, b = map(int, input().split())
lst = [True for i in range(b + 1)]

lst[0], lst[1] = False, False

for i in range(int(b ** 0.5) + 1):
    if lst[i]:
        for j in range(i+i, len(lst), i):
            lst[j] = False
            
for i in range(a, b + 1):
    if lst[i]:
        print(i)