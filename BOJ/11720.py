case = int(input())
num_lst = list(input())
answer = 0

for i in range(case):
    answer += int(num_lst[i])
    
print(answer)