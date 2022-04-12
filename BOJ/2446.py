a = int(input())

for i in range(a):
    print(' ' * (i), end = '')
    print('*' * (2 * (a - i) - 1))
    
for i in range(1, a):
    print(' '*(a - i - 1), end = '')
    print('*' * (2 * i + 1))