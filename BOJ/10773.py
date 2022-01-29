case = int(input())
num_lst = []

for i in range(case):
    num_lst.append(int(input()))
    if num_lst[-1] == 0:
        num_lst.pop(-1)
        num_lst.pop(-1)
        
print(sum(num_lst))