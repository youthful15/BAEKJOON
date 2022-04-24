m = int(input())
lst = []

for _ in range(m):
    cnt = input().split()
    if cnt[0] == 'add':
        lst.append(int(cnt[1]))
    elif cnt[0] == 'remove':
        if int(cnt[1]) in lst:
            lst.remove(int(cnt[1]))
    elif cnt[0] == 'check':
        if int(cnt[1]) in lst:
            print(1)
        else:
            print(0)
    elif cnt[0] == 'toggle':
        if int(cnt[1]) in lst:
            lst.remove(int(cnt[1]))
        else:
            lst.append(int(cnt[1]))
    elif cnt[0] == 'all':
        lst = [i for i in range(1, 21)]
    else:
        lst = []