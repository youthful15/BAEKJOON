for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    time_list = list(map(int, input().split()))
    t = 0       # 지난 시간
    cnt = 0     # 손님수 카운트
    bbang = 0
    time_list.sort()
    max_t = max(time_list)
    print(time_list)
    
    while t < max_t and bbang >= 0:
        if time_list[cnt] < t:
            bbang -= 1
            cnt += 1
            continue
        t += M
        bbang += K
        
    if t > max_t:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')