lst = [int(input()) for i in range(9)]

a = sum(lst) - 100

try:
    for i in range(8):
        for j in range(i + 1, 9):
            if lst[i] + lst[j] == a:
                lst.pop(i)
                lst.pop(j - 1)
except:
    pass
        
for key in sorted(lst):
    print(key)