cnt, mok = map(int, input().split())
lst = list(map(int, input().split()))
max_num = 0


for i in range(cnt - 2):
    for j in range(1 + i, cnt - 1):
        for k in range(1 + j, cnt):
            if 0 <= mok - (lst[i] + lst[j] + lst[k]) < mok - max_num:
                max_num = lst[i] + lst[j] + lst[k]
            if max_num == mok:
                break
            
print(max_num)