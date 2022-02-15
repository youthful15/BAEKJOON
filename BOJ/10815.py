m = int(input())
good_set = set(map(int, input().split()))
n = int(input())
check_lst = list(map(int, input().split()))



for check in check_lst:
    if {check} & good_set:
        print(1, end=' ')
    else:
        print(0, end=' ')