import sys

case = int(sys.stdin.readline())
lst = [0 for i in range(case)]

for i in range(case):
    lst[i] = int(sys.stdin.readline())
    
bin_dic = {}
bin_lst = []

# bin_dic에 등장 빈도 정리
for num in lst:
    bin_dic[num] = bin_dic.get(num, 0) + 1

cnt_lst = list(bin_dic.values())
num_lst = list(bin_dic.keys())
    
# 최빈값 모음
for i in range(len(num_lst)):
    if cnt_lst[i] == max(cnt_lst):
        bin_lst += [num_lst[i]]
    
print(round(sum(lst) / case))
print(sorted(lst)[case // 2])
if len(bin_lst) >= 2:
    print(sorted(bin_lst)[1])
else:
    print(bin_lst[0])
print(max(lst) - min(lst))