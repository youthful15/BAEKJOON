import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lst = [int(input()) for i in range(k)]
    
end = max(lst)
start = 1

while start <= end:
    find = (end + start) // 2
    answer = 0
    
    for camp in lst:
        answer += (camp // find)
        
    if answer >= n:
        start = find + 1
    else:
        end = find - 1
        
print(end)