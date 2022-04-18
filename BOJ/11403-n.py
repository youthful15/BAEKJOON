def find(s, g):
    for k in lst[g]:
        if arr[s][k]:
            return
        else:
            arr[s][k] = 1
            find(s, k)
    

n = int(input())
lst = [[] for _ in range(n)]

for j in range(n):
    l = list(map(int, input().split()))
    for i in range(n):
        if l[i]:
            lst[j].append(i)
            
print(lst)
            
arr = [[0] * n for _ in range(n)]

for i in range(n):
    for l in lst[i]:
        arr[i][l] = 1
        find(i, l)
        
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print('')