case = int(input())
for i in range(case):
    sero, garo, n = map(int, input().split())
    dong = n // sero + 1
    ho = n % sero
    if sero == 1:
        print(f'{n}01')
    elif garo == 1:
        if n > 10:
            print(f'1{n}')
        else:
            print(f'10{n}')
    else:
        if dong > 10:
            print(f'{ho}{dong}')
        else:
            print(f'{ho}0{dong}')