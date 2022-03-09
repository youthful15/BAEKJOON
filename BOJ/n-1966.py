for i in range(int(input())):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    a = lst[m]
    answer = 1
    last = 'a'
    
    for num in lst:
        if num > lst[m]:
            answer += 1
            keep = num
            
    for i in range(m + 1, m + n):
        if lst[i % n] == keep:
            last = i % n
            
    print(f'last:{last}')
            
    if last != 'a':
        for i in range(last + 1, last + n):
            if i % n == m:
                break
            elif lst[i % n] == lst[m]:
                answer += 1
                
    print(answer)