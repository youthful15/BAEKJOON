import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a = int(input())
    lst = [list(map(int, input().split())) for _ in range(a)]
    ans = 0
    
    lst.sort()
    b = lst[0][1]
    print(lst)
    
    for i in lst:
        if i == lst[0]:
            ans += 1
        elif i[1] < b:
            ans += 1
            b = i[1]
            
    print(ans)