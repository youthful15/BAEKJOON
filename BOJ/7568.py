a = int(input())
lst = [0 for i in range(a)]
final = [1 for i in range(a)]

for i in range(a):
    lst[i] = list(map(int, input().split()))
    
for i in range(a):
    for j in range(a):
        if lst[i][0] < lst[j][0]:
            if lst[i][1] < lst[j][1]:
                final[i] += 1
    print(final[i], end = ' ')