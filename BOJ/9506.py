while True:
    a = int(input())
    if a == -1:
        break
    lst = []
    for num in range(1, a):
        if a % num == 0:
            lst.append(num)
    if sum(lst) == a:
        print(f'{a} = {" + ".join(map(str, lst))}')
    else:
        print(f'{a} is NOT perfect.')