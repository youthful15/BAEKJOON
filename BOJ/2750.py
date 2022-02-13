a = int(input())
lst = [-1001 for i in range(1000)]

for i in range(a):
    lst[i] = int(input())
    
lst.sort()
    
for i in range(-a, 0, 1):
    print(lst[i])