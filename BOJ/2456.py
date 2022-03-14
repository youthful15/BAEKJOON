v1 = v2 = v3 = []
x = int(input())

for i in range(x):
    a, b, c = map(int, input().split())
    print(a, b, c)
    v1 += [a]
    v2 += [b]
    v3 += [c]

print(v1, v2, v3)
cnt = 0

lst = [sum(v1), sum(v2), sum(v3)]
max_lst = []

max_num = max(sum(v1), sum(v2), sum(v3))

for i in range(len(lst)):
    if lst[i] == max_num:
        max_lst += [i]

print(lst)
print(max_lst)
        
if len(max_lst) == 1:
    print(lst.index(max_num) + 1, max_num)
elif len(max_lst) == 2:
    for i in range(x):
        if sum(lst[max_lst[0]][0:i]) > sum(lst[max_lst[1]][0:i]):
            print(max_lst[0] + 1, max_num)
            break
        elif sum(lst[max_lst[0]][0:i]) < sum(lst[max_lst[1]][0:i]):
            print(max_lst[1] + 1, max_num)
            break
    else:
        print(0, max_num)