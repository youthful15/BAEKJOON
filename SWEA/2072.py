q_num = int(input())

for i in range(q_num):
    sum_num = 0
    num_list = list(map(int, input().split()))
    for j in num_list:
        if j % 2 == 1:
            sum_num += j
    print('#{0} {1}'.format(i + 1, sum_num))