import sys

case = int(sys.stdin.readline())
lst = [0 for i in range(10000)]
index_lst = []

for i in range(case):
    a = int(sys.stdin.readline())
    lst[a - 1] += 1

for i in range(len(lst)):
    if lst[i] != 0:
        index_lst.append(i)
        
for i in index_lst:
    for j in range(lst[i]):
        print(i + 1)