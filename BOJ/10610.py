case = list(map(int, input()))

if 0 not in case:
    print('-1')
elif sum(case) % 3 != 0:
    print('-1')
else:
    case.remove(0)
    case.sort(reverse = True)
    for num in case:
        print(num, end = '')
    else:
        print(0)