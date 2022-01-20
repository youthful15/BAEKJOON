case = int(input())

for i in range(case):
    print(f'#{i+1}',end=' ')
    num_list = list(map(int,input().split()))
    max_num = num_list[0]
    for num in num_list:
        if num > max_num:
            max_num = num
    print(max_num)
