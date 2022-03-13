cnt = int(input())

lst = [False] + [i for i in range(1, cnt + 1)] + [False]
idx = 0
ans = []

for i in range(cnt):
    a = int(input())
    
    if idx < a:
        while idx < a:
            idx += 1
            if lst[idx]:
                ans += ['+']
            
        if lst[idx]:
            ans += ['-']
            lst[idx] = False
            idx -= 1
        else:
            ans = ['NO']
        
    else:
        while idx > a:
            if lst[idx]:
                lst[idx] = False
                ans += ['-']
            idx -= 1
            
        if lst[idx]:
            lst[idx] = False
            ans += ['-']
            idx -= 1
        else:
            ans = ['NO']
    
    if ans == ['NO']:
        break
            
for i in ans:
    print(i)