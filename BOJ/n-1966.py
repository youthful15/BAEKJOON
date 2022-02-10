from collections import deque

case = int(input())

for i in range(case):
    num, q = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 1
    
    if num == 1:
        print(1)
        continue
    
    for num in lst:
        if num > lst[q]:
           cnt += 1
           
    close = [10 for i in range(num)]
    
    for j in range(num):
        if 0 < lst[j] - lst[q] < close[j]:
            close[j] = j
            
    print(close)
            
    