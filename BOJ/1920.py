import sys

a = int(sys.stdin.readline())
a_lst = list(map(int, sys.stdin.readline().split()))
b = int(sys.stdin.readline())
b_lst = list(map(int, sys.stdin.readline().split()))

dict = {}

for num in a_lst:
    if num not in dict:
        dict[num] = 1
        
for num in b_lst:
    if num in dict:
        print(1)
    else:
        print(0)