import sys
input = sys.stdin.readline

m = int(input())

lst = [0] * 21

for _ in range(m):
    cnt = input().split()

    if cnt[0] == 'add':
        lst[int(cnt[1])] = 1
    elif cnt[0] == 'remove':
        if lst[int(cnt[1])]:
            lst[int(cnt[1])] = 0
    elif cnt[0] == 'check':
        print(lst[int(cnt[1])])
    elif cnt[0] == 'toggle':
        if lst[int(cnt[1])]:
            lst[int(cnt[1])] = 0
        else:
            lst[int(cnt[1])] = 1
    elif cnt[0] == 'all':
        lst = [1] * 21
    else:
        lst = [0] * 21
