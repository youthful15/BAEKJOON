a = int(input())
b = int(input())
lst = []

for i in range(a, b + 1):
    if i ** 0.5 == int(i ** 0.5):
        lst += [i]
        
if lst:
    print(sum(lst))
    print(lst[0])
else:
    print(-1)