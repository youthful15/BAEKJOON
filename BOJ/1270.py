for _ in range(int(input())):

    lst = list(map(int, input().split()))
    dict = {}

    for i in range(lst[0]):
        if lst[i + 1] in dict:
            dict[lst[i + 1]] += 1
        else:
            dict[lst[i + 1]] = 1

    for (k, v) in dict.items():
        if v > lst[0] / 2:
            print(k)
            break
    else:
        print('SYJKGW')
