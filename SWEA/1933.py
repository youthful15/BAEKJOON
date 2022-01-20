case = int(input())

for i in range(1, case + 1):
    if case % i == 0:
        print(i,end=' ')