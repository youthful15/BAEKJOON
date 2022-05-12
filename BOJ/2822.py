lst = [int(input()) for _ in range(8)]
lst2 = sorted(lst)
lst3 = []

print(sum(lst2[3:8]))

for i in range(5):
    lst3.append(lst.index(lst2[7 - i]) + 1)
    
for i in sorted(lst3):
    print(i, end = ' ')