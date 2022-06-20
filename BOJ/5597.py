lst = [0] * 31

for i in range(28):
    a = int(input())
    lst[a] = 1

for i in range(1, len(lst)):
    if not lst[i]:
        print(i)
