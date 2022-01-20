case = int(input())
for i in range(case):
    print(f'#{i+1}',end=' ')
    date = input()
    if not 12 > int(date[4:6]) > 0:
        print("-1")
    elif int(date[4:6]) == 2 and not 28 >= int(date[6:8]) > 0:
        print("-1")
    elif int(date[4:6]) in [1, 3, 5, 7, 8, 10, 12] and not 31 >= int(date[6:8]) > 0:
        print("-1")
    elif int(date[4:6]) in [4, 6, 9, 11] and not 30 >= int(date[6:8]) > 0:
        print("-1")
    else:
        print(f'{date[0:4]}/{date[4:6]}/{date[6:8]}')
    