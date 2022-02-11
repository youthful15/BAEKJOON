a = int(input())

for i in range(a, 0, -1):
    print(' ' * (i - 1), end='')
    print('*' * ((a - i + 1) * 2 - 1))