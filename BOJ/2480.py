dict = {i : 0 for i in range(1, 7)}
lst = list(map(int, input().split()))

for i in lst:
    dict[i] += 1
    
for i in range(1, 7):
    if dict[i] == 3:
        print(i * 1000 + 10000)
        break
    elif dict[i] == 2:
        print(i * 100 + 1000)
        break
else:
    print(max(lst) * 100)