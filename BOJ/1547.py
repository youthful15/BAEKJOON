m = int(input())
lst = [0, 1, 0, 0]

for i in range(m):
    a, b = map(int, input().split())
    lst[a], lst[b] = lst[b], lst[a]
    
print(lst.index(1))