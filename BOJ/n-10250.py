from __future__ import generators


case = int(input())
for i in range(case):
    sero, garo, n = map(int, input().split())
    dong = n // sero + 1
    ho = n % sero
    if ho == 0:
        ho == sero
    if dong > 10:
        print(f'{ho}{dong}')
    else:
        print(f'{ho}0{dong}')