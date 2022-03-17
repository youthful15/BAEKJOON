a = int(input())
for i in range(a):
    print(' ' * (a - 1 - i), end='')
    print('*' * (2 * i + 1))
for i in range(1, a):
    print(' ' * i, end='')
    print('*' * (2 * (a - 1 - i) + 1))
          