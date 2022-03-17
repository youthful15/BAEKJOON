a = int(input())

for i in range(a):
    print('*' * (i + 1),end = '')
    print(' ' * ((a - 1 - i) * 2),end = '')
    print('*' * (i + 1))
for i in range(a - 1, 0, -1):
    print('*' * i,end = '')
    print(' ' * (a - i) * 2,end = '')
    print('*' * i)