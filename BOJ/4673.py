lst = [True for i in range(0, 10001)]
lst[0] = False

for i in range(len(lst)):
    if lst[i] == True:
        print(i)
        a = i
        while True:
            crush = list(map(int, str(a)))
            a = a + sum(crush)
            try:
                if lst[a]:
                    lst[a] = False
                else:
                    break
            except:
                break