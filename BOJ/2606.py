def find(s):
    v[s] = 1
    
    for i in graph[s]:
        if v[i] == 0:
            find(i)
            v[i] = 1


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
v = [0] * (n + 1)

find(1)
print(v.count(1) - 1)