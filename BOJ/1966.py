case = int(input())

for i in range(case):
    num, q = map(int, input().split())
    lst = [0 for i in range(num)]
    lst = list(map(int, input().split()))
    cnt = 1
    
    for number in lst:
        if lst[q] < number:
            cnt += 1
            
    print(cnt)
        