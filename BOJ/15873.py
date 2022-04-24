lst = list(input())

if len(lst) == 2:
    print(int(lst[0]) + int(lst[1]))
elif len(lst) == 3 and lst[1] == '0':
    print(int(lst[0]) * 10 + int(lst[2]))
elif len(lst) == 3:
    print(int(lst[0]) + int(lst[1]) * 10)
else:
    print(int(lst[0]) * 10 + int(lst[2]) * 10)
    