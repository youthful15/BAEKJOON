n, k = map(int, input().split())
lst = [0] * 100001
lst[n] = 1
new_lst = [n]
ans = 0

if n < k:
    while True:
        temp_lst = []
        ans += 1
        for l in new_lst:
            for j in (l+1, l-1, l*2):
                if 0 <= j <= 100000 and lst[j] == 0:
                    lst[j] = 1
                    temp_lst.append(j)
        if lst[k] == 1:
            break
        new_lst = temp_lst
else:
    ans = n - k
    
print(ans)
            