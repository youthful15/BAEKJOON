a, kill = map(int, input().split())
lst = [True for i in range(a)]
kill_lst = []
kill_idx = kill - 1
cnt = a

while True in lst:
    while cnt < kill:
        if kill_idx >= a:
            kill_idx -= a
        if lst[kill_idx] == True:
            cnt += 1
            kill_idx += 1
        else:
            kill_idx += 1
                    
    lst[kill_idx - 1] = False
    if kill_idx >= a:
        kill_idx -= a
    kill_lst.append(kill_idx + 1)
    cnt = 0

answer = str(kill_lst).replace('[','<')
print(answer.replace(']','>'))