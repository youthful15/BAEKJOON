n = input()
lst = [0] + [0 for i in range(9)]

for i in n:
    lst[int(i)] += 1
    
lst[6] = (lst[6] + lst[9]) // 2 + (lst[6] + lst[9]) % 2
lst[9] = 0

print(max(lst))