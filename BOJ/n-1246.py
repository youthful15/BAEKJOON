import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = []
sum_num = max_num = max_idx = 0

for i in range(m):
    lst += [int(input())]
    
lst.sort(reverse=True)
    
for i in lst:
    for j in range(m):
        if lst[j] <= i:
            if j > n:
                sum_num += i * n
            else:
                sum_num += i * j
            break
    
    if sum_num > max_num:
        max_num = sum_num
        max_idx = i
    sum_num = 0
    
print(max_idx, max_num)