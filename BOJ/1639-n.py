a = input()
i = len(a) // 2

if len(a) // 2 == 0:
    while i > 0:
        for j in range((len(a) // 2 - i + 1) * 2 - 1):
            sum1 = sum2 = 0
            for k in range(i):
                sum1 += int(a[k + j])
                sum2 += int(a[k + i + j])
            if sum1 == sum2:
                print(i * 2)
                i = 0
                break
        i -= 1

else:
    while i > 0:
        for j in range((len(a) // 2 - i + 1) * 2):
            sum1 = sum2 = 0
            for k in range(i):
                sum1 += int(a[k + j])
                sum2 += int(a[k + i + j])
            if sum1 == sum2:
                print(i * 2)
                i = 0
                break
        i -= 1


if i == 0:
    print(0)
