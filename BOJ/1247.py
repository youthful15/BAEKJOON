import sys
input = sys.stdin.readline

for _ in range(3):
    a = int(input())
    lst = [int(input()) for i in range(a)]
    ans = sum(lst)
        
    if ans > 0:
        print('+')
    elif ans < 0:
        print('-')
    else:
        print(0)