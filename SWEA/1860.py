for tc in range(1, int(input()) + 1):
    n, m, k = map(int, input().split())
    lst = list(map(int, input().split()))
    bbang = 0
    
    for i in range(len(lst)):
        lst[i] = lst[i] // m
        
    dict = {i : 0 for i in range(101)}
    
    for i in lst:
        dict[i] += 1
        
    for i in range(11112):
        if dict[i]:
            bbang -= dict[i]
            dict[i] = 0
        if bbang < 0:
            print(f'#{tc} Impossible')
            break
        bbang += k
    else:
        print(f'#{tc} Possible')
        