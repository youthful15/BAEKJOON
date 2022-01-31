case = int(input())

for i in range(case):
    lst = list(map(int, input().split()))
    print(sorted(lst)[-3])