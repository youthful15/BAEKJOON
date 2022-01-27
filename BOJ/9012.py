case = int(input())
for i in range(case):
    a = list(input())
    if len(a) % 2 == 1:
        print('NO')
        continue
    for i in range(len(a) // 2):
        try:
            if a.index('(') < a.index(')'):
                a.pop(a.index('('))
                a.pop(a.index(')'))
            else:
                print('NO')
                break
        except:
            print('NO')
            break
    else:
        print('YES')