case = int(input())
num_list = list(map(int, input().split()))
max_number, min_number = num_list[0], num_list[0]

for now_num in num_list:
    if max_number < now_num:
        max_number = now_num
    if min_number > now_num:
        min_number = now_num
        
print(f'{min_number} {max_number}')