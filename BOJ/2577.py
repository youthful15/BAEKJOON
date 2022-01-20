a = int(input())
b = int(input())
c = int(input())

list_abc = list(str(a * b * c))
num_lst = [0 for i in range(10)]

for i in range(10):
    for j in list_abc:
        if i == int(j):
            num_lst[i] += 1
    print(num_lst[i])