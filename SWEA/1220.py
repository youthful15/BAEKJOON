for tc in range(1, 11):
    n = int(input())
    lst = [list(map(int, input().split())) for i in range(n)]
    answer = 0
    
    for i in range(n):
        new_lst = []
        for j in range(n):
            if lst[j][i]:
                new_lst += [lst[j][i]]
        for k in range(len(new_lst) - 1):
            if new_lst[k] == 1 and new_lst[k+1] == 2:
                answer += 1
                
    print(f'#{tc} {answer}')