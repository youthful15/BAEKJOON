case = int(input())

for i in range(case):
    a, b = input().split()
    lst = list(b)
    for j in b:
        print(j * int(a),end='')
    print('')