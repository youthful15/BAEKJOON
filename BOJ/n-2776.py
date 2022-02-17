import sys
input = sys.stdin.readline

for i in range(int(input())):
    a = int(input())
    lst_a = list(map(int, input().split()))
    b = int(input())
    lst_b = list(map(int, input().split()))
    
    for what in lst_b:
        if what in lst_a:
            print(1)
        else:
            print(0)