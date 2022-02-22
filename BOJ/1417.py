lst = []
cnt = 0
max_num = 0

for _ in range(int(input())):
    lst += [int(input())]
    
while lst[0] != max(lst) or lst[0] in lst[1:len(lst)]:
    for i in range(len(lst)):
        if max_num <= lst[i]:
            max_num = lst[i]
            max_idx = i
            
    lst[0] += 1
    lst[max_idx] -= 1
    cnt += 1
    max_num = 0
    
print(cnt)