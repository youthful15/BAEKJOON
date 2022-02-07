lst = [0 for i in range(5)]
for i in range(5):
    lst[i] = int(input())
    if lst[i] < 40:
        lst[i] = 40
    
print(int(sum(lst) / 5))