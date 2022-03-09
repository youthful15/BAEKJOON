lst = [False] + [i for i in range(1, int(input()) + 1)]
idx = 0
ans = []

for i in range(int(input())):
    a = int(input())
    
    if idx < a:
        while idx != a:
            if lst[idx]:
                ans += ['+']
                idx += 1
        ans += ['-']
        lst[idx] = False
        idx -= 1
        
    elif idx > a:
        while idx >= a:
            if lst[idx]:
                lst[idx] = False
                ans += ['-']
                idx -= 1
                
print(lst)
print(ans)