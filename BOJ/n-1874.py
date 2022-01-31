case = int(input())
bef = 0

for i in range(case):
    num = int(input())
    while num != bef:
        if num > bef:
            bef += 1
            print('+')
        else:
            bef -= 1
            print('-')